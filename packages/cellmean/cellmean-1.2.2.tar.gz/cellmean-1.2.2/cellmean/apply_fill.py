from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import data, img_as_float, io

def bilateral_denoising(image, sigma_color=0.05, sigma_spatial=15):
    if isinstance(image, str):  
        image = io.imread(image)
    elif not isinstance(image, np.ndarray):
        raise ValueError("Input must be either a file path or a numpy array.")
        
    image_noise = denoise_bilateral(image, sigma_color=sigma_color, sigma_spatial=sigma_spatial, channel_axis=-1)
    return image_noise

from skimage.filters import gaussian, sobel

def gaussian_filter(image, sigma=3):
    if isinstance(image, str):  
        image = io.imread(image)
    elif not isinstance(image, np.ndarray):
        raise ValueError("Input must be either a file path or a numpy array.")
    
    image_gaussian = gaussian(image, sigma=sigma, channel_axis=-1)
    return image_gaussian

def sobel_edge(image):
    edge_sobel = sobel(image)
    return edge_sobel


import mahotas 
from scipy import ndimage
import numpy as np

def mean_filter(image, Bc=None):
    if isinstance(image, str):  
        image = io.imread(image)
    elif not isinstance(image, np.ndarray):
        raise ValueError("Input must be either a file path or a numpy array.")
    
    if Bc is None:
        Bc = np.ones((3, 3))
    
    image_mean = mahotas.mean_filter(image, Bc=Bc)
    return image_mean