# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:12:13 2022

@author: Lenovo
"""

from skimage import io
from matplotlib import pyplot as plt

img= io.imread("images/barbara.png", as_gray=True)

from skimage.transform import rescale, resize, downscale_local_mean

rescaled_img= rescale(img, 1.0/4.0, anti_aliasing=True)
resized_img=resize(200,200)

#-----------------------------------------------
# Edge Detection

from skimage import io
from matplotlib import pyplot as plt

img= io.imread("images/barbara.png", as_gray=True)

from skimage.filters import roberts, sobel, scharr, prewitt

edge_roberts= roberts(img)
edge_sobel=sobel(img)
edge_scharr=scharr(img)
edge_prewitt=prewitt(img)

fig, axes= plt.subplots(nrows=2, ncols=2,
                        sharex= True, figsize=(8,8))
ax=axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("Original Image")

ax[1].imshow(edge_roberts, cmap=plt.cm.gray)
ax[1].set_title("Roberts Edge Detection")


ax[2].imshow(edge_sobel, cmap=plt.cm.gray)
ax[2].set_title("Sobel")

ax[3].imshow(edge_scharr, cmap=plt.cm.gray)
ax[3].set_title("Scharr")

for a in ax:
    a.axis('off')
    
plt.tight_layout()
plt.show()

# Canny Edge Detector (Output is binary)

from skimage import io
from matplotlib import pyplot as plt

img= io.imread("images/barbara.png", as_gray=True)

from skimage.feature import canny
edge_canny=canny(img, sigma=2) # sigma=amount of edge detection
plt.imshow(edge_canny)

#-----------------------------------------------
# Deconvolution (Sharpening the image)

from skimage import io
from matplotlib import pyplot as plt

img= io.imread("images/barbara.png", as_gray=True)

from skimage import restoration
 
import numpy as np

psf=np.ones((3,3))/9 # point spread function

deconvolved , _ = restoration.unsupervised_wiener(img, psf)

plt.imsave("images/deconvolved.jpg", deconvolved, cmap="gray")










