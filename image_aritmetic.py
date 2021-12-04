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

# Define M matrix
M = 100 * np.ones(image.shape, dtype='uint8')
brighter = cv2.add(image, M)
cv2.imshow('Brighter Image', brighter)
cv2.waitKey(0)

darker = cv2.subtract(image, M)
cv2.imshow('Darker Image', darker)
cv2.waitKey(0)
