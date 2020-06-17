import numpy as np 

"""
Este submodulo contiene distintos thresholds tanto unicos como variables por el nivel aplicado 

Los implementados hasta el momento son:

1- universal: utiliza la ecuacion:
    \sigma ^ 2 


"""

def universal_threshold( sigma, image ):
    rows, cols = image.shape 
    len_data = rows * cols 

    return (sigma**2) * np.sqrt( 2* np.log10( len_data ) )

def bayes_threshold( sigma, image, coeffs ):
    details = coeffs[1:]
    thresholds = []
    for (H, _, _), i in zip( details, range( len( details ) )):
        ( rows, cols ) = H.shape
        sigmaY2 = np.sum( H * H ) / ( rows * cols )
        sigmaX = np.sqrt( np.max( [ sigmaY2 - sigma ** 2, 0 ] ) )
        if sigmaX <= 0:
            t = np.max( np.abs( H ) )
        else: 
            t = sigma ** 2 / sigmaX
        
        thresholds.append( [ t, t, t ] )

    return thresholds
