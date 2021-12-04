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

# Now Let's Translate our Image
# First we will Declare the Translation Matrix M to be a floating point matrix in the form ([[1, 0, tx], [0, 1, ty]])
M = np.float32([[1, 0, 50], [0, 1, 50]])

# Now Let's Shift our Image
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Image', shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, 50, 50)
cv2.imshow('Shifted2 Image', shifted)
cv2.waitKey(0)

# Another Example
M = np.float32([[1, 0, -50], [0, 1, -50]])

# Now Let's Shift our Image
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Another Shifted Image', shifted)
cv2.waitKey(0)
shifted = imutils.translate(image, -50, -50)
cv2.imshow('Shifted2 Image', shifted)
cv2.waitKey(0)
