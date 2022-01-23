# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:33:44 2022

@author: Lenovo
"""

from PIL import Image
img= Image.open("images/foggysf2.jpg")
print(img.mode) #RGB, Gray etc.
print(img.size)

small_img=img.resize((200,300))
small_img.save("images/small_foggy.jpg")

img.thumbnail((200,300))

#---------------------------------------

# Cropping
from PIL import Image
img= Image.open("images/foggysf2.jpg")
cropped_img= img.crop((0,0,300,300))
cropped_img.save("images/cropped.jpg")

#---------------------------------------

# Rotation
from PIL import Image
img= Image.open("images/foggysf2.jpg")
img90=img.rotate(90, expand= True)

#---------------------------------------

# Flipping
from PIL import Image
img= Image.open("images/foggysf2.jpg")
img_flipLR= img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipTB=img.transpose(Image.FLIP_TOP_BOTTOM)

#---------------------------------------

# Converting to Graylevel

from PIL import Image
img= Image.open("images/foggysf2.jpg")
gray_img=img.convert("L")

#---------------------------------------

# Multiple Images

from PIL import Image
import glob

path= "images/*"

for file in glob.glob(path):
    print(file)
    a=Image.open(file) # Opens each file.
    rotate45=a.rotate(45, expand=True)
    rotate45.save(file+"_rotated45.png", "PNG")
    
    
















