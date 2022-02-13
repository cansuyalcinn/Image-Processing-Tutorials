# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:47:18 2022

@author: Lenovo
"""

import cv2
import numpy as np 
from matplotlib import pyplot as plt


img = cv2.imread("images/cameraman.tif", 0) # 0: graylavel
# Histogram equalization
eq_img=cv2.equalizeHist(img)

# plt.hist(img.flat, bins=100 , range=(0,255))
# flattens our 2d array into one dimension so that we can look at the histogram

plt.hist(eq_img.flat, bins=100 , range=(0,255))

cv2.imshow("Equalized image", eq_img)
cv2.imshow("Original image", img)

# Adaptive Histogram Equalization
'''It does this histogram equalization in small patches. 
It does best contrast limiting. It is called CLAHE.
'''

clahe= cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img= clahe.apply(img)
cv2.imshow("CLAHE image", cl_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------------
# Thresholding (histogram based thresholding)

import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread("images/pout.tif", 0) # 0: graylavel
clahe= cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img= clahe.apply(img)

plt.hist(cl_img.flat, bins=100 , range=(50,200))

# Histogram Segmentation (Using thresholding)

ret, thresh1 = cv2.threshold(cl_img,130, 100, cv2.THRESH_BINARY)
# All the graylevels have the value of 100.

ret, thresh2 = cv2.threshold(cl_img, 130, 255, cv2.THRESH_BINARY_INV)
# All the graylevels have the value of 255.

ret, thresh3 = cv2.threshold(cl_img, 0, 255, cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
# OTSU based thresholding

cv2.imshow("ORIGINAL image", img)
cv2.imshow("Binary threshold1", thresh1)
cv2.imshow("Binary threshold2", thresh2)
cv2.imshow("OTSU", thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()





