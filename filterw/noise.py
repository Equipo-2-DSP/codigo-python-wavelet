import numpy as np


def noise_2d( img, std ):
    row, col = img.shape
    mean = 0
    gauss = np.random.normal( mean, std ** 2, (row, col) )
    gauss = gauss.reshape( row, col )
    img_noise = img + gauss 
    return img_noise / np.max( img_noise )

def noise( signal, mean ,std ):
    n = len( signal )
    return signal + np.gauss( mean, std ** 2, n )