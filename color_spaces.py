# Import Required Packages
import cv2
import numpy as np

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)

# Now Let's Visualize Different Color Spaces, RGB, HSV, L*a*b
# Original Image
cv2.imshow('Original BGR', image)
cv2.waitKey(0)

# RGB Image
RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', RGB)
cv2.waitKey(0)

# Gray Image
Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY', Gray)
cv2.waitKey(0)

# HSV Image
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', HSV)
cv2.waitKey(0)

# L*a*b Image
Lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b', Lab)
cv2.waitKey(0)
