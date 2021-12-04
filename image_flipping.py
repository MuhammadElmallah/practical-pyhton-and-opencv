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

# Now Let's filp the image
# Flipping the Image Vertically
flipped = cv2.flip(image, 0)
cv2.imshow('Vertically Flipped Image', flipped)
cv2.waitKey(0)

# Flipping the Image Horizontally
flipped = cv2.flip(image, 1)
cv2.imshow('Horizontally Flipped Image', flipped)
cv2.waitKey(0)

# Flipping the Image Horizontally and Vertically
flipped = cv2.flip(image, -1)
cv2.imshow('Horizontally Vertically Flipped Image', flipped)
cv2.waitKey(0)
