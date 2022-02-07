# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:13:17 2022

@author: Lenovo
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread("images/barbara.png")
kernel= np.ones((5,5), np.float32)/25 # normalizing

filt_2d= cv2.filter2D(img, -1, kernel) # convolution
blur= cv2.blur(img, (5,5))
gaussian_blur=cv2.GaussianBlur(img, (5,5), 0)
median_blur=cv2.medianBlur(img, 5)
bilateral_blur=cv2.bilateralFilter(img, 9, 75, 75)

# Edges
edges=cv2.Canny(img, 100,100)
cv2.imshow("Edges", edges)

cv2.imshow("original", img)
cv2.imshow("2d custom filter", filt_2d)
cv2.imshow("Blur", blur)
cv2.imshow("Gaussian", gaussian_blur)
cv2.imshow("Median", median_blur)
cv2.imshow("Bilateral Filter", bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()