# Import Required Packages
import cv2
import numpy as np
import imutils

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)
cv2.imshow('Image', image)
cv2.waitKey(0)

# Calculating the Aspect Ratio
old_width = image.shape[1]
old_height = image.shape[0]
height = 500
r = height / old_height
width = int(r * old_width)
dim = (height, width)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)

# Using the imutils
new_image = imutils.resize(image, 224, 224)
cv2.imshow('Resized 2 Image', new_image)
cv2.waitKey(0)
