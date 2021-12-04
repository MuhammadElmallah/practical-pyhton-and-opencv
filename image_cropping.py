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

# Now Let's Crop the image
cropped = image[30:100, 50:160]
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
