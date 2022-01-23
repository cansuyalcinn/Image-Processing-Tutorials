# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 21:53:08 2022

@author: Lenovo
"""

from scipy import misc
img= misc.imread("images/barbara.png")
print(type(img))

from skimage import io
img2= io.imread("C:/Users/Lenovo/Documents/Image Processing Self Study Codes/images/barbara.png",
                as_gray=True)
print(type(img2))
print(img2.shape)

mean_gray=img2.mean() # mean, max, min

#------------------------------------

# Flipping

from scipy import ndimage
from skimage import io, img_as_ubyte
import numpy as np
from matplotlib import pyplot as plt


img2= img_as_ubyte(io.imread("C:/Users/Lenovo/Documents/Image Processing Self Study Codes/images/barbara.png",
                as_gray=False))
flippedLR=np.fliplr(img2) # left right
flippedUD=np.flipud(img2) # up down

plt.subplot(2, 1,1)
plt.imshow(img2, cmap="Greys")
plt.subplot(2, 2,3)
plt.imshow(flippedLR, cmap="Blues")
plt.subplot(2, 2,4)
plt.imshow(flippedUD, cmap="hsv")

rotated= ndimage.rotate(img2, 45, reshape=False)
plt.imshow(rotated)


#------------------------------------

# Image Filtering

uniform_filter=ndimage.uniform_filter(img2, size=3) 
# Blurring filter
plt.imshow(uniform_filter)

gaussian_filtered= ndimage.gaussian_filter(img2, sigma=11)
plt.imshow(gaussian_filtered)

median_filtered= ndimage.median_filter(img2,3)
# Preserves the edges opposite as gaussian
plt.imshow(median_filtered)

# Edge detection
sobel_img=ndimage.sobel(img2, axis=0)
plt.imshow(sobel_img)





























