# Trabajo final de DSP 

## Integrantes del grupo:

1) Marin Santiago 
2) Gatica Isaias
3) Saez Lautaro Andres
4) Vidman Xavier

## Modulos utilizados: 

1) pyWavelets: este modulo implementa las funciones basicas para obtener la transformada de **Wavelet**.
2) matplotlib: contiene las funciones basicas para realizar graficos en 2D y 3D.
3) numpy: contiene todo tipo de herramientas matematicas.
   

## Modulos propios:

### filterw

En este modulo se encuentran funciones basicas para el filtrado de ruido, las cuales se describen a continuación.

#### ImageFilter 

Es una clase la cual tiene los siguiente atributos 

1) image: privado - imagen a filtrar 
2) threshold: privado - funcion de threshold que se utilizara para el filtro
3) threshold_type: privado - es el tipo de threshold aplico, siendo unico o variable por nivel 
4) sigma_image: privado - el desvio estandar de la imagen.

#### Threshold 

Contiene algunas funciones de threshold como 

1) universal_threshold: $\sigma^2 \sqrt{ 2log( n ) }$
2) bayes_threshold: se toma $ \max{ |H| } $ si $\sigma_X=0$, si no $\sigma^2 / \sigma_X$ donde $\sigma_X=\sqrt{\max{ \sum{ H.H - \sigma^2, 0 } }}$.

#### Noise 

Este pequeño submodulo contiene funcionene para agregar ruido gaussiano en 1 y 2d.