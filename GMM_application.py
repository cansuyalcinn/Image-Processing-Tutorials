# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:31:28 2022

@author: Lenovo
"""

# GMM Application

''' 
GMM is a soft clustering technique.
It uses expectation maximization.
Expectation step: Calculating the probablities for each datapoint.
Maximization setp: Updating mean, variance and weight each time.
'''

import numpy as np
import cv2
from sklearn.mixture import GaussianMixture as GMM

img = cv2.imread("images/onion.png")
img2=img.reshape((-1,3))

gmm_model= GMM(n_components=2, covariance_type="tied").fit(img2)

gmm_labels= gmm_model.predict(img2)

original_shape=img.shape
segmented= gmm_labels.reshape(original_shape[0], original_shape[1])

cv2.imwrite("segmendted_gmm.png", segmented)







