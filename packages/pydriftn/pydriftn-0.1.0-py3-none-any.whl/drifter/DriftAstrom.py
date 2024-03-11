from collections import Counter
import math
import numpy as np
import pandas as pd
import scipy as scp
from statistics import mean

#for cosmic ray removal
import astroscrappy

import astropy
import astropy.units as u
from astropy.coordinates import match_coordinates_sky, SkyCoord
from astropy.io import fits
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from astropy.visualization.wcsaxes import SphericalCircle
from astropy.wcs import WCS
from astropy.wcs.utils import fit_wcs_from_points

#for centroiding
from astropy.convolution import convolve
from astropy.convolution.kernels import Model2DKernel
from astropy.modeling.models import Box2D
from photutils.centroids import centroid_sources, centroid_com
from photutils.detection import find_peaks

from photutils.aperture import CircularAperture, SkyCircularAperture
import matplotlib.pyplot as plt
from matplotlib import colors

from multiprocessing import Pool
from functools import partial
import logging
from Utils import ImageImporter, append_to_fits_header


file_handler = logging.FileHandler("logfile.log")
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


class DriftAstrometry():
    '''
    This object class finds and matches drift centroids in a VR image
    to the input catalogue(s) and updates the VR image with new WCS.

    Parameters
    ----------
    driftscan_image_path: str
        Local path to VR FITS file.
    photometry_catalogue: str
        Local path to photometry_catalogue.csv.
    astrometry_catalogue: str
        Local path to astrometry_catalogue.csv.
    ccd_names: list
        A list of all CCD names to be included in the catalogue. 
        # TODO: set a default value.
    track_rate: float
    background_thresh: float or array_like 
        The image background or a defined threshold level to search for flux peaks.
        Below background values, no peaks will be defined (i.e for faint drifts).
    anchor: str
        A string to represent the anchor location (x,y).
        For now, this is a linear shift in y:
            'r' is a leftways move to +y_offset, 
            'l' is a rightways move to -y_offset, 
            'm' is midway, and keeps the anchor at the centroid location.
    n_brightest_drifts: int
        The number of sources to search for. 
        From decreasing brightness the first n_brightest_drifts will be returned.
    perform_cosmicray_removal: boolean
        Option to perform cosmic ray removal at the beginning of the pipeline.
    '''

    def __init__(self, driftscan_image_path, photometry_catalogue, astrometry_catalogue, ccd_names, 
                track_rate, background_thresh, anchor, n_brightest_drifts=200, perform_cosmicray_removal=False):
        '''
        Initialises DriftAstrometry with driftscan_image, photometry_catalogue, astrometry_catalogue, bias_files,
        ccd_names, track_rate, background_thresh, anchor, n_brightest_drifts, perform_cosmicray_removal.
        '''

        self.driftscan_image = driftscan_image_path #'/Users/reneekey/Documents/drift_testset/c4d_2019B0071_exp917982.fits'
        self.photometry_catalogue = pd.read_csv(photometry_catalogue) # path to photometry_catalogue.csv TODO: for matching and writing centroid positions.
        self.ccd_names = ccd_names

        self.track_rate = track_rate
        self.background = background_thresh
        self.anchor = anchor
        self.n_brightest_drifts = n_brightest_drifts
        self.perform_cosmicray_removal = perform_cosmicray_removal  
        
        # externally cross-match with Gaia to the closest match
        #self.astrometry_catalogue = pd.read_csv(astrometry_catalogue)
    
    @staticmethod
    def make_odd(val):
        '''
        A simple static function that ensures an integer is odd.
        If value is not odd, add 1 to make it odd.

        Parameter
        ---------
        val: float or int
            The input value.
        
        Returns
        -------
        odd_value: int
            The output odd integer.
        '''
        try:
            i = int(val)
        except ValueError:
            logging.error('Invalid input value.')

        if i%2 == 0:
            odd_value = i + 1
        else:
            odd_value = i

        return odd_value
    

    def import_image(self, filepath, ccd_name):
        '''
        Imports a fits image and transforms into WCS.

        Parameters
        ----------
        filepath: str
            Local path to the FITS file.
        ccd_name: str
            The name of the ccd image extension in the fits file.

        Returns
        -------
        fits_header: ``astropy.io.fits.header.Header`` class object.
        ccd_data: float ``numpy.ndarray`` of the image.
        ccd_header: FITS header class.
        wcs_fits: ``astropy.wcs.WCS`` class object.
        clean_mask: boolean ``numpy.ndarray``
            The cosmic ray mask (boolean) array with values of True where there are cosmic ray detections.
        clean_data: float ``numpy.ndarray``
            The cleaned data array after the cosmic ray removal.
        '''
        
        Image = ImageImporter(ccd_name, filepath)

        fits_header = Image.get_fits_header()
        ccd_header, ccd_data = Image.get_fits_image()
        wcs_fits = Image.wcs_transform(ccd_header)
        
        if self.perform_cosmicray_removal:
            clean_mask, clean_data = Image.cosmicray_removal(ccd_hdr=ccd_header, ccd_data=ccd_data)
            # TODO: save  
        else:
            # TODO: read from the fits file assuming it's saved there as an extension.
            clean_mask = clean_data = None

        return fits_header, ccd_data, ccd_header, wcs_fits, clean_mask, clean_data
    
    
    def drift_width(self, fwhm_estimate, unit='pixel', pixelscale=0.27):
        '''
        Estimates the width of a star.

        Parameters
        ----------
        fwhm_estimate: float
            The input estimated width of the star.
        unit: str
            The unit of measurement for the fwhm_estimate.
            If the fwhm_estimate is in arcsec, it will be converted into pixel. 
        pixelscale: float
            The pixelscale of the image. 

        Returns
        -------
        fwhm_estimate: float
            The estimated width of the star, in pixels.
        '''
        #Estimate width of star (here we use Noirlab Community pipeline FITs headers in this function call)
        if unit == 'arcsec':
            fwhm_estimate = fwhm_estimate * pixelscale
        
        return fwhm_estimate


    def drift_length(self, track_rate, exp_time, unit='arcsec', pixelscale=0.27):
        '''
        Calculates the drift length from the given tracking rate, exposure duration and pixelscale.

        Parameters
        ----------
        track_rate: float
        exp_time: int
            The exposure duration of the image.
        unit: str
            The unit of measurement for the track rate.
        pixelscale: float
            The pixelscale of the image.

        Returns
        -------
        length: float
            The drift length.
        '''
        #calculates drift length given user defined tracking rate, and FITs header cards for the
        #exposure duration and pixelscale
        #NOTE: rate is given in arcsec/second ---> exp_time must be in seconds
        
        if unit == 'arcsec':
            length = track_rate * exp_time / pixelscale
        
        if unit == 'pixel':
            length = track_rate * exp_time
        
        return length


    def drift_model(self, a, b, unit='pixel', pixelscale=0.27):
        '''
        Defines a Box2D model that makes a theoretical model drift.

        Parameters
        ----------
        a: float
            The width in y direction of the box.
        b: float
            The width in x direction of the box.
        unit: str
            The unit of measurement for the widths.
        pixelscale: float
            The pixelscale of the image.

        Returns
        -------
        model: ``astropy.modeling.functional_models.Box2D`` class object.
        '''
        #define a Box2D model that makes a theoretical model drift given drift rate, exposure time
        #or width, length depending on unit
        
        #unit are pixel or 'arcsec'
        if unit == 'arcsec':
            a = a * pixelscale
            b = b * pixelscale
            
        model = Box2D(x_0=0, x_width=b, y_0=0, y_width=a)
        return model


    def drift_centroids(self, ccd_data, background, wcs_fits, model):
        '''
        Finds centroids of the drifts in an image.

        Parameters
        ----------
        ccd_data: float ``numpy.ndarray`` of the image.
            The drifted VR image.
        background: float or array_like 
            The image background or a defined threshold level to search for flux peaks.
            Below background values, no peaks will be defined (i.e for faint drifts).
        wcs_fits: ``astropy.wcs.WCS`` class object.
            The original WCS of the image.
        model: ``astropy.modeling.functional_models.Box2D`` class object.
            A simplistic model of the typical driftscan (2D rectangle of constant flux).

        Returns
        -------
        drift_map: ``astropy.table.Table`` class object
            A table containing the x and y pixel location of the peaks and their values
        drift_conv: ``numpy.ndarray``
            The convolution result of the image with the drift kernel.
        '''
        
        shape = DriftAstrometry.make_odd(model.x_width.value), DriftAstrometry.make_odd(model.y_width.value) #must be integer values for kernel
        drift_kernel = Model2DKernel(model, x_size=int(shape[0]*2 - 1)) #what does xsize do?
        drift_conv = convolve(ccd_data, drift_kernel)
        drift_map = find_peaks(drift_conv, background, box_size=20, npeaks = self.n_brightest_drifts, wcs = wcs_fits) #redefine 
        
        x_peaks = drift_map['x_peak']
        y_peaks = drift_map['y_peak']
        
        x, y = centroid_sources(ccd_data, x_peaks, y_peaks, box_size=shape, centroid_func=centroid_com)
        
        drift_map['x_cent'] = x
        drift_map['y_cent'] = y
        
        skycoord = wcs_fits.pixel_to_world(drift_map['x_cent'], drift_map['y_cent'])
        drift_map['ra_cent'] = [i.ra.deg for i in skycoord]
        drift_map['dec_cent'] = [i.dec.deg for i in skycoord]
        
        return drift_map, drift_conv


    def project_centroids(self, centroid_table, wcs_fits, anchor, model):
        '''
        Take a centroided drift position and shift it left or right to the start of end of the drift, or keep it
        at the midpoint of the drift.
        
        This function anchors the drift ra, dec to a specific point along the drift. 
        The exposure starts with specific coordinates of the field, and our specific tracking rate in 
        declination (along the y-axis) builds the trail of the drift. Technically the WCS is built from the
        initial starting image of the start at exp_time = 0 at position (x, y) = (0,0), 
        and at exp_time = 20 seconds, the star is elsewhere on the detector image (+0, + 40) pixels.
        
        Our positions in the WCS shift should be measured with respect to the star position at the beginning
        of the exposure.
        
        The opposite anchor point ('r') would be equivalent to a reversed tracking rate of -0.5 arcsecs/sec in dec. 
        I've included this point as a input in case other drift datasets have different tracking directions. 
        
        Eventually this could become more sophisticated, where the user has tracking_vector = (0.5, 0.1) in (ra, dec)
        and the projection would work out the relevant x and y anchor points for the starting location of the source. 
        
        Parameters
        ----------
        centroid_table: ``pandas.DataFrame`` 
            A table of the centroid locations of driftscans.
        wcs_fits: ``astropy.wcs.WCS`` class object.
            The original WCS of the image.
        anchor: str
            A string to represent the anchor location (x,y).
            For now, this is a linear shift in y:
                'r' is a leftways move to +y_offset, 
                'l' is a rightways move to -y_offset, 
                'm' is midway, and keeps the anchor at the centroid location.
        model: ``astropy.modeling.functional_models.Box2D`` class object.
            An astropy 2D rectangular model of the driftscan.

        Returns
        -------
        centroid_table: ``pandas.DataFrame`` 
            The updated table of the centroid locations of driftscans.
        '''
        
        #from the centroid locations, plop down a centroided model and use a specific x,y pixel as the anchor
        #for all drifts. i.e 'l' = left, 'r' = right, 'm' = middle/centroid....
        
        half_y = model.y_width.value/2
        anchor_x = 0  #no linear shift to centroid midline position
        
        if anchor == 'r':
            anchor_y = -half_y  #no linear shift to centroid midline position       
        elif anchor == 'l':
            anchor_y = half_y  
        elif anchor == 'm':
            anchor_y = 0
        else:
            logger.warn("Invalid anchor input value: {}. Options: 'r', 'l', or 'm'.".format(anchor))
            anchor_y = 0
            
        centroid_table['x_a'] = centroid_table['x_cent'] + anchor_x
        centroid_table['y_a'] = centroid_table['y_cent'] + anchor_y
        
        
        skycoord = wcs_fits.pixel_to_world(centroid_table['x_a'], centroid_table['y_a'])
        centroid_table['ra_a'] = [i.ra.deg for i in skycoord]
        centroid_table['dec_a'] = [i.dec.deg for i in skycoord]

        return centroid_table


    def match_drift_ref(self, ref_cat_pos, centroid_pos, wcs_fits):
        '''
        Matches ra and dec positions on sky between the reference stars and the drifts.

        Parameters
        ----------
        ref_cat_pos: list or tuple 
            List of tuple of ra, dec positions for main catalogue.
        centroid_pos: table or list 
            Table or list of ra, dec positions for VR images.
        wcs_fits: ``astropy.wcs.WCS`` class object.
            The original WCS of the image.

        Returns
        -------
        w_SHIFT: ``astropy.wcs.WCS`` class object.
            The new WCS.
        '''
        
        #match between ra and dec positions on sky between the reference stars and the drifts
        #Noted (20th Feb 2024) that this function is slow, and we could speed up using Stilts

        ref_coords = SkyCoord(ref_cat_pos['ra'].tolist()*u.deg, ref_cat_pos['dec'].tolist()*u.deg, frame='fk5')
        drift_coords = SkyCoord(centroid_pos['skycoord_peak.ra'].tolist()*u.deg, centroid_pos['skycoord_peak.dec'].tolist()*u.deg, frame='fk5')

        idx, d2d, d3d = drift_coords.match_to_catalog_sky(ref_coords)

        matched_refs = ref_coords[idx]

        #apply linear shift (Renee to test on Thursday/Friday)
        ref_pixel = wcs_fits.world_to_pixel(ref_coords)
        matched_ref_x = [ref_pixel[0][i] for i in idx]
        matched_ref_y = [ref_pixel[1][i] for i in idx]
        
        # TODO: errors in matching shape, are these supposed to be an array or an integer?
        #xshift = ref_pixel[0] - centroid_pos['x_a']
        #yshift = ref_pixel[1] - centroid_pos['y_a']

        # NOTE: (temporary) take the mean offset
        xshift = mean([a - b for a, b in zip(matched_ref_x, centroid_pos['x_a'].tolist())])
        yshift = mean([a - b for a, b in zip(matched_ref_y, centroid_pos['y_a'].tolist())])
        drift_xy = np.array([[x + xshift for x in centroid_pos['x_a']], [y + yshift for y in centroid_pos['y_a']]])
        
        #take the matched drift x and y positions to the reference star skycoordinates in g, r images
        w_SHIFT = fit_wcs_from_points(xy=drift_xy, world_coords=matched_refs, projection='TAN')
        
        return w_SHIFT


    def update_image_wcs(self, ccd_name):
        '''
        Updates an image header with new WCS and creates a table of drift centroids and matched reference stars.

        Parameters
        ----------
        ccd_name: str
            The name of the ccd image extension in the fits file.
        
        Returns
        -------
        drift_map_df: ``pandas.DataFrame`` 
            The table of the centroid locations of driftscans.
        '''
        fits_header, ccd_data, ccd_header, wcs_fits, crmask, cleanarr = self.import_image(self.driftscan_image, ccd_name)
        
        if cleanarr:
            data = cleanarr
        else:
            data = ccd_data

        fwhm_estimate = ccd_header['FWHM']
        pixscale = fits_header['PIXSCAL1']
        drift_w = self.drift_width(fwhm_estimate, 'pixel', pixscale)

        exp_time = fits_header['EXPTIME']
        drift_l = self.drift_length(self.track_rate, exp_time, 'arcsec', pixscale)

        # TODO: params for drift_model function? 
        # Do we want these as user inputs or would these be outputs of drift_width and drift_length functions?
        model = self.drift_model(5,40)
        
        drift_map_table, convolution_res = self.drift_centroids(ccd_data, self.background, wcs_fits, model)
        
        drift_map_df = drift_map_table.to_pandas()
        drift_map_df = self.project_centroids(drift_map_df, wcs_fits, self.anchor, model)

        photometry_cat_subset = self.photometry_catalogue[self.photometry_catalogue['chp'] == ccd_name]
        new_wcs = self.match_drift_ref(photometry_cat_subset, drift_map_df, wcs_fits)

        # TODO: write to header?
        #append_to_fits_header(ccd_header, ['x_vr', 'y_vr'], [x_vr, y_vr], [])
        return drift_map_df


    def update_whole_image(self):
        '''
        Updates the headers of all of the specified CCDs with new WCS and
        compiles drift centroids and the matched reference stars for all CCDs in the VR/driftscan image.


        Returns
        -------
        centroids_df: ``Pandas.DataFrame``
            A Pandas dataframe of all drift centroids found and matched with the reference stars.
        '''

        with Pool() as p:
            centroids = p.map(self.update_image_wcs, self.ccd_names)
            centroids_df = pd.concat(centroids)

        output_csv_path = 'centroids.csv'
        centroids_df.to_csv(output_csv_path, index=False)

        return centroids_df
