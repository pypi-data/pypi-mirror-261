from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from astropy.wcs import WCS

import astroscrappy
import warnings
import numpy as np

import logging


file_handler = logging.FileHandler("logfile.log")
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

class ImageImporter:
    '''
    This class object imports the data from the given FITS file path and ccd_name.
    Also includes a cosmic ray removal function. 

    Parameters
    ----------
    ccd_name: str
        The name of the CCD.
    filepath: str
        The local path to the FITS file.
        
    '''
    def __init__(self, ccd_name, filepath):
        '''Initialises ImageImporter with ccd_name and filepath.'''
        
        self.ccd = ccd_name
        self.filepath = filepath


    def open_fits(self):
        '''
        Opens a FITS file.

        Returns
        -------
        fits_file: ``astropy.io.fits.HDUList`` class
            ``HDUList`` containing all of the header data units in the file.
        '''

        try:
            fits_file = fits.open(self.filepath)
        except OSError as oe:
            logger.error("Cannot open file: {}.".format(filepath), exc_info=True)
            fits_file = None
        except FileNotFoundError as fe:
            logger.error("Cannot find file: {}.".format(filepath), exc_info=True)
            fits_file = None
        
        return fits_file


    def get_fits_header(self):
        '''
        Retrieves the FITS header.

        Returns
        -------
        hdr: ``astropy.io.fits.header.Header`` class object.
        '''

        fits_file = self.open_fits()
        if fits_file:
            with fits_file:
                try:
                    hdr = fits_file[0].header
                except AttributeError:
                    logger.error("Error opening file: {}.".format(self.filepath), exc_info=True)
                    hdr = None
        else:
            hdr = None 
        self.hdr = hdr

        return hdr

    
    def get_pixscale(self, primary_header):
        '''
        Retrieves pixelscale information from the primary header of a FITS file.

        Returns
        -------
        pixscale: float
            The pixel scale of the image.
        '''

        pixscale = primary_header['PIXSCAL1']
        self.pixscale = pixscale
        return pixscale


    def get_fits_image(self):
        '''
        Retrieves the header and data for a given extension of the FITS file.

        Returns
        -------
        ccd_hdr: ``astropy.io.fits.hdu.compressed.header.CompImageHeader`` class object.
        ccd_data: ``numpy.ndarray`` of the image.
        '''

        fits_file = self.open_fits()
        if fits_file:
            with fits_file:
                try:
                    ccd_hdr = fits_file[self.ccd].header 
                    ccd_data = fits_file[self.ccd].data
                except (KeyError, AttributeError) as e:
                    logger.error("CCD name not found for file: {}.".format(self.filepath), exc_info=True)
                    ccd_hdr = ccd_data = None                             
        else:
            ccd_hdr = ccd_data = None
        self.ccd_hdr = ccd_hdr
        self.ccd_data =  ccd_data # previously self.data
        
        return ccd_hdr, ccd_data


    def get_background(self, ccd_header, ccd_data):
        '''
        Retrieves the background value from a FITS image.

        Parameters
        ----------
        ccd_header: ``astropy.io.fits.hdu.compressed.header.CompImageHeader`` class object.
        ccd_data: ``numpy.ndarray`` of the image.
        
        Returns
        -------
        background: float
            The estimated background value.
        '''

        try:
            background = ccd_header['AVSKY']
        except KeyError as k:
            background = sigma_clipped_stats(ccd_data, sigma=3.0)[1] #(median value)
        
        return background

    def wcs_transform(self, header):
        '''
        Gets WCS transformations for the FITS file.

        Returns
        -------
        ``astropy.wcs.WCS`` class
        
        '''

        if header:
            try:
                wcs_fits = WCS(self.ccd_hdr)
            except (MemoryError, ValueError, KeyError) as e:
                logger.error("Failed to perform WCS transformations for file: {}.".format(self.filepath), exc_info=True)
                wcs_fits = None
            else: 
                logger.info("{}: successfully transformed the fits file header into WCS.".format(self.filepath))  
        else: 
            wcs_fits = None
        self.wcs_fits = wcs_fits # previously self.wcs

        return wcs_fits       


    def cosmicray_removal(self, ccd_hdr, ccd_data, gain_keyword = ['GAINA', 'GAINB'], 
                          saturation_keyword = ['SATURATA', 'SATURATB'], readnoise_keyword = ['RDNOISEA', 'RDNOISEB']):
        '''
        Detects and removes cosmic rays in the FITS image.

        Parameters
        ----------
        ccd_hdr: ``astropy.io.fits.hdu.compressed.header.CompImageHeader`` class object.
        ccd_data: ``numpy.ndarray`` of the image.
        gain_keyword: list
            Keywords for the gain values of interest.
        saturation_keyword: list
            Keywords for the gain values of interest.
        readnoise_keyword: list
            Keywords for the gain values of interest.

        Returns
        -------
        clean_mask: boolean ``numpy.ndarray``
            The cosmic ray mask (boolean) array with values of True where there are cosmic ray detections.
        clean_data: float ``numpy.ndarray``
            The cleaned data array after the cosmic ray removal.
            
        '''
        
        gain_median = np.median([ccd_hdr[gain] for gain in gain_keyword])
        readnoise_median = np.median([ccd_hdr[readnoise] for readnoise in readnoise_keyword])
        saturation_median = np.median([ccd_hdr[saturate] for saturate in saturation_keyword])

        self.gain = gain_median
        self.readnoise = readnoise_median
        self.saturation = saturation_median
        
        try:
            clean_mask, clean_data = astroscrappy.detect_cosmics(ccd_data, gain=gain_median,
                                                                readnoise=readnoise_median, satlevel=saturation_median, cleantype='medmask')
        except Exception as e: # TODO: specify the error
            logger.error("Cannot generate cosmic ray mask.", exc_info=True)
            clean_mask = clean_data = None
            
        self.cr_mask = clean_mask
        self.clean_data = clean_data

        # TODO: save as extension

        return clean_mask, clean_data


def append_to_fits_header(self, ccd_hdr, keys:list, values:list, comments:list):
    '''
    Appends lists of values and comments to a list of keys in an image header with parallel iteration.

    Parameters
    ----------
    ccd_hdr: ``astropy.io.fits.hdu.compressed.header.CompImageHeader`` class object.
    keys: list
        A list of keyword names to be added to / updated in the image header.
    values: list
        A list of values to be added to the paired keys in the image header.
    comments: list
        A list of comments to be added along with the paired values, to the paired keys in the image header.

    '''
    # always new keys?
    # set strict=True?

    for k, v, c in zip(keys, values, comments):
        ccd_hdr[k] = (v, c)
