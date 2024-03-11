import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import scipy.stats                         # for Pearson r
from scipy.optimize import curve_fit
from scipy.stats import norm
from scipy.integrate import simps
import os
import logging


file_handler = logging.FileHandler("logfile.log")
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

class TimeSeriesGenerator:
    def __init__(self)
        self.ccd_image = '/Users/reneekey/Documents/drift_testset/VR_S31_ori_exp1058800.fits'
        self.bias_frame1 = '/Users/reneekey/Documents/drift_testset/VR_bias_zri_exp043052.fits'
        self.bias_frame2 = '/Users/reneekey/Documents/drift_testset/VR_bias_zri_exp043115.fits'
        
        #reference stars in a list - This will be a read in from another function
        self.s_list = [(1942,2543), (1665, 1757), (1156, 1495), (1479,1141), (725, 3298), (972, 201), (2021, 1577),
                        (324, 247), (247, 1202), (817, 2497), (170, 1295), (894, 1356), (771, 833), (1620, 252)]
        self.L = len(self.s_list) 
        self.LI = 32   # fit to flat part of DSI: x = 10:41 incl : 32 pixels
    
    
    def L3(self, y, LF, SF, MF):    
        N = 2.75                                           # ignore background for a start
        P = LF*SF**N / (np.abs(y-MF)**N + SF**N) 
        return P


    #make a little more streamlined with photutils
    def S_fun1(self, xs, ys):         # xs and ys are LH end of driftscan to nearest pix           
        # estimate sky level with a couple of 2-sigma clip cycles and subtract from star        
        star = scidata[ys-5:ys+6, xs-6:xs+45]            # star has shape (11,51)           
        sky = scidata[ys-35:ys+35,xs-15:xs+55]           # sky has shape (70,70)            
        sky_flat = sky.flatten()                                                            
        m_sky = sky_flat.mean()                                                             
        std_sky = sky_flat.std()                                                            
        
        c0 = abs(sky_flat - m_sky)< 2.0 * std_sky        # clip cycle0                      
        sky_clip0 = sky_flat[c0]                                                            
        skybar0 = np.median(sky_clip0)                       
        skysig0 = np.std(sky_clip0)
        
        c1 = abs(sky_clip0 - skybar0)< 2.0 * skysig0     # clip cycle1
        sky_clip1 = sky_clip0[c1]
        skybar1 = np.median(sky_clip1)
        skysig1 = np.std(sky_clip1)
        
        star = star - skybar1                            # subtract sky from the star

        return star

    
    def debiasing(self, image_data, bias_files:list):
        #debiasing step
        # INPUT: opened image data of a fits file, a list of paths to bias files.
        # Output:  debiased data
        biases = []
        for b in bias_files:
            try:
                bias_file = fits.open(b)
            except OSError as oe:
                logger.error("Cannot open file: {}.".format(b), exc_info=True)
                continue
            except FileNotFoundError as fe:
                logger.error("Cannot find file: {}.".format(b), exc_info=True)
                continue
            else:
                with bias_file:
                    try:
                        bias = bias_file[36].data # 36?
                        biases.append(bias)
                    except IndexError, AttributeError:
                        logger.error("Index error.", exc_info=True)

        median_bias = np.nanmedian(biases, axis = 0)
        scidata = image_data-bias
        
        return scidata

    
    def extract_template_stars(self):
        # Is this the correct function name?
                                                         # 20 
        xstar = np.zeros(self.L,dtype='int32')
        ystar = np.zeros(self.L,dtype='int32')
        star = np.zeros((self.L,11,51))                             # flat part of star DSI is x = 10:41

        for k in np.arange(self.L):                                                     
            xstar[k] = self.s_list[k][0]
            ystar[k] = self.s_list[k][1]    
            
            star[k,:,:] = S_fun1(xstar[k],ystar[k])          
            
        # save star data
        # np.save('star',star)        
        # read as np.load('star.npy')           

        #This needs to be fixed!!

        logger.info("{} template stars extracted.".format(self.L))
        return star
    

    def perform_l3_fitting(star):
        L0 = np.zeros((self.L,self.LI))                      # parameters for DSI for L3 fits to each of 20 stars
        S0 = np.zeros((self.L,self.LI))
        M0 = np.zeros((self.L,self.LI))

        eL = np.zeros((self.L,self.LI))                      # errors for L0,S0,M0
        eS = np.zeros((self.L,self.LI))
        eM = np.zeros((self.L,self.LI))

        y = np.arange(11)                           # pixel coordinate across the drift

        for k in np.arange(self.L):                     # loop over the L=20 template stare

            Py = star[k,:,:]                        # shape(Py) = (11,51)

            for i in np.arange(self.LI):                 # fit Py(x) for x = 10:41 incl = 32 pixels
                                                    # flat part of DSI is x = 9:40 inclusive                           
                P0 = [Py[:,i+10].max(),2.,3.5]
                #print(P0)
                try: 
                    popt1, pcov1 = curve_fit(self.L3, y, Py[:,i+10],P0)          # catch curve_fit error
                except RuntimeError:
                    logger.error("continuing after RTE at k,i = {}, {}.".format(k,i))
                    continue
                else: 
                    L0[k,i] = popt1[0]                  # shape(L0) = (20,32)
                    S0[k,i] = popt1[1]
                    M0[k,i] = popt1[2]
                    perr = np.sqrt(np.diag(pcov1))      # errors for L0,S0,M0
                    eL[k,i]=perr[0]
                    eS[k,i]=perr[1]
                    eM[k,i]=perr[2]
        
        logger.info("L3 fits done for {} stars".format(self.L)) 

        # what does this do? what needs to be returned?
        T = np.sum(star,axis=1)[:,10:42]            # shape(T) = (L,32)
        L0S0 = L0*S0                                # shape(L0S0) = (L,32)

        ratioT_L0S0 = (T / L0S0).mean()
        stdT_L0S0 = (T / L0S0).std()
        SNR_T = np.mean(T,axis=1) / np.std(T,axis=1)
        SNR_L0S0 = np.mean(L0S0,axis=1) / np.std(L0S0,axis=1)

        return # TODO


#YET TO BE CLEANED UP

'''m_best = np.zeros(L, dtype='int64')         # index
r_best = np.zeros(L)
r = np.zeros((L,L))
T_corr = np.zeros((L,LI))
SNR_T_corr = np.zeros(L)

# ------------- normalise T to their median         
                
T_norm = (T.T / np.median(T, axis=1)).T               # T normalised to median(T)                                      

# ------------- calculate Pearsonr correlations all star pairs  (20,20) 

for k in np.arange(L): 
    for m in np.arange(L):
        r[k,m],p = scipy.stats.pearsonr(T_norm[k],T_norm[m])
             
# ------------- for each k, find index m_best for star with the second-largest r:  i.e  largest r with r != 1 
      
    m_best[k] = np.argsort(r[k,:])[L-2]                                        

# ------------- divide each star by the other star in the set of L stars with which it had the largest r

    T_corr[k] = T_norm[k,:] / T_norm[m_best[k],:]
    
# ----------- now calculate the SNR for the corrected spectra
#         the r-parameter for the best match to star k is r[k,m_best[k]]

    SNR_T_corr[k] = np.median(T_corr[k,:])/np.std(T_corr[k,:])
    r_best[k] =  r[k,m_best[k]]  '''
