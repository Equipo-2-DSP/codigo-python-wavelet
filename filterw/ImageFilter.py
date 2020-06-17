import numpy as np 
import pywt
import cv2 
from skimage.restoration import estimate_sigma

class ImageFilter(  ):

    def __init__(self, threshold, threshold_type , image):
        self._threshold = threshold
        self._threshold_type = threshold_type
        if( type( image ) == str  ):
            image = cv2.imread( image, cv2.IMREAD_GRAYSCALE )
        self._image = image
        self._sigma_image = estimate_sigma( image )


    def filter( self, wavelet='haar', mode='hard' ):
        rows, cols = self._image.shape
        len_data = rows * cols 
        wavelet = pywt.Wavelet( wavelet )
        level = pywt.dwt_max_level( data_len= len_data, filter_len=wavelet.dec_len )
        wavelet_coeff = pywt.wavedec2( self._image, wavelet ,level=level )

        if( self._threshold_type == 'unique'  ):
            filter_coeff = self._global_threshold( wavelet_coeff, mode )
        elif( self._threshold_type == 'for-levels' ):
            filter_coeff = self._levels_threshold( wavelet_coeff, mode )
        else: 
            raise( f"La funcion umbral seleccionada no es valida, por favor elija un tipo valida:\n ${ self.threshold_types() }" )
        
        return pywt.waverec2( filter_coeff, wavelet )
    

    def wavelet_list( self ):
        return pywt.waveletlist()

    def threshold_types(self ):
        return ['for-levels', 'unique']

    def _global_threshold(self, coeffs, mode ):

        threshold = self._threshold( self._sigma_image, self._image )

        coeffs[1:] = [ [ pywt.threshold( detail, value=threshold, mode=mode ) for detail in coeff ] for coeff in coeffs[1:] ]

        return coeffs

    def _levels_threshold( self, coeffs, mode ):

        thresholds = self._threshold( self._sigma_image, self._image, coeffs )

        coeffs[1:] = [ tuple([ pywt.threshold( detail, value=thresholds[i][j], mode=mode ) for detail, j in zip( coeff, range(3) ) ]) for coeff, i in zip( coeffs[1:], range( len( coeffs ) - 1 ) ) ]

        return coeffs
