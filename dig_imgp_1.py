# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:25:48 2022

@author: Lenovo
"""

from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_float # Converts image to float

my_image=io.imread("images/foggysf2.jpg")
print(my_image)
print(my_image.min(), my_image.max())
# Image is between 0-219.

my_float_image=img_as_float(my_image)
print(my_float_image.min(), my_float_image.max())
# Image is between 0.0 to 0.85.
# These two images are the same. 

random_image= np.random.random([500,500])
plt.imshow(random_image)

# Reducing all values by their half.
dark_image= my_image*0.5
print(dark_image)

# Slicing
my_image[10:200, 10:200, :] =[255, 0,0]
plt.imshow(my_image)