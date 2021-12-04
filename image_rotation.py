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

# Now Let's Rotate our Image
(h, w) = image.shape[0:2]
center = (w//2, h//2)
# First we will Declare the Translation Matrix M
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, 45)
cv2.imshow('Rotated 2 Image', rotated)
cv2.waitKey(0)
