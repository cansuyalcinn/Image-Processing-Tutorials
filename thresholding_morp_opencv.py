# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 12:39:32 2022

@author: Lenovo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread("images/barbara.png", 0)
# Denosing --> median: Good for denoising also retains edges. 
# One of the best for denoising: Non local means denoising from scikit-image.

median= cv2.medianBlur(img, 3)

plt.hist(img.flat, bins=100, range=(0,255))

# OTSU based thresholding -- Automatic thresholding
ret, thresh1= cv2.threshold(median, 0, 255, cv2.THRESH_BINARY+ cv2.THRESH_OTSU)

# Morphological Operations
kernel= np.ones((3,3), np.uint8)
erosion=cv2.erode(thresh1, kernel, iterations=1)
# Application of erosion+dilation (opening)
dilation=cv2.dilate(erosion, kernel, iterations=1)

# Opening 
opening=cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)

# Closing
closing=cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)

cv2.imshow("original image",img)
cv2.imshow("Median image",median)
cv2.imshow("OTSU image",thresh1)
cv2.imshow("Eroded image",erosion)
cv2.imshow("Erosion+dilation image",dilation)
cv2.imshow("Opening image",opening)
cv2.imshow("Closing image",closing)

cv2.waitKey(0)
cv2.destroyAllWindows()