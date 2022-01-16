# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:52:47 2022

@author: Lenovo
"""

# Pillow
from PIL import Image
import numpy as np

img= Image.open("Images/foggysf2.jpg")
print(type(img)) # Image type is not np.array.
img.show()
print(img.format)

# Converting into np.array
img1=np.asarray(img)
print(type(img1))

#-------------------------------------------

# Matplotlib / Pyplot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img2= mpimg.imread("Images/foggysf2.jpg")
print(type(img2)) # Image type is np.array.
print(img2.shape)
plt.imshow(img2)
plt.colorbar()

#-------------------------------------------

# Scikit image
from skimage import io, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt
image=io.imread("Images/foggysf2.jpg")
print(type(image)) # Image type is np.array.
plt.imshow(image)

# Convert as float
img_float= img_as_float(image) # Scales between 0-1
print(img_float)

# Or we could do
image2=io.imread("Images/foggysf2.jpg").astype(np.float)
print(image2) # Converts between 0-255


#-------------------------------------------

# OpenCv

import cv2
import matplotlib.pyplot as plt

image3= cv2.imread("Images/foggysf2.jpg")
image3_gray= cv2.imread("Images/foggysf2.jpg",0)
image3_color= cv2.imread("Images/foggysf2.jpg",1)

plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
# After the conversion, the image is correct. 

plt.imshow(image3_gray)

cv2.imshow("gray image",image3_gray )
cv2.imshow("color image", image3_color)

cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------

# Reading Multiple Images

import cv2
import glob

path = "Images/*"
for file in glob.glob(path):
    print(file)
    a=cv2.imread(file)
    print(a)
    c= cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow( "Color Image", c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

















