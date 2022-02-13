# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:46:00 2022

@author: Lenovo
"""

'''
# https://docs.opencv.org/3.4/db/d27/tutorial_py_table_of_contents_feature2d.html
Key point: A point of interest.
Feature detector detects key points, feature descriptor describes these key points. 
'''
#-------------------------------------------------
# Harris Detector : Key point detector
# Corner points are detected. 
# Works on gray level, float32 images.

import cv2
import numpy as np

img= cv2.imread("images/barbara.png")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray= np.float32(gray)

harris= cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
# blockSize: size of neighborhoos considered.

img[harris>0.01*harris.max()]=[255,0,0] # Blue
'''
Getting only certain points where harris value is greater than 1 percent of harris.max()
Noise is gone.
'''
cv2.imshow("Harris", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------
# Shi-Tomasi Corner Detector & Good Features to Track  : Key point detector

import cv2
import numpy as np

img= cv2.imread("images/football.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray= np.float32(gray)

corners= cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
# corners is 50 points of x and y coordinates. 

corners= np.uint0(corners)

for i in corners:
    x,y=i.ravel()
    print(x,y)
    cv2.circle(img, (x,y), 3, 255 , -1)
    
    
cv2.imshow("Corners", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------
# FAST Feature Detector
# Detector should be used with a decriptor. For example, descriptor BRIEF

import cv2
import numpy as np

img= cv2.imread("images/football.jpg", 0)

detector= cv2.FastFeatureDetector_create(100)

kp=detector.detect(img, None) 
# List of the key points

img2= cv2.drawKeypoints(img, kp, None, flags=0)

cv2.imshow("FAST Feature Detector", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------
# ORB (Oriented FAST and Rotated BRIEF)
# Combination of both. 

import cv2
import numpy as np

img= cv2.imread("images/onion.png", 0)
orb= cv2.ORB_create(50)

kp, des= orb.detectAndCompute(img, None)

img2= cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("ORB", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()














