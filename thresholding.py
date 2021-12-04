# Import Required Packages
import cv2
import numpy as np
import mahotas

# Create a variable containing the path to the image
image_path = 'images.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)
image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Converting the image to Gray and Applying Guassian Blurring with sigma = 5
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
guass = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('Gaussian Blurred Image', guass)
cv2.waitKey(0)

# Now Let's Apply Simple Thresholding
# Applying simple thresholding methods requires human intervention. We must specify a threshold value T.
# All pixel intensities below T are set to 0. And all pixel intensities greater than T are set to 255.
(T, thresh) = cv2.threshold(guass, 174, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Image', thresh)
cv2.waitKey(0)
(T, threshinv) = cv2.threshold(guass, 174, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Inverse Image', threshinv)
cv2.waitKey(0)

# Applying the Threshold Inverse as a mask
masked = cv2.bitwise_and(image, image, mask=threshinv)
cv2.imshow('Thresholding and Masking', masked)
cv2.waitKey(0)

# Adaptive Thresholding, we no longer need to specify the threshold manually
# Using Mean Method
thresh = cv2.adaptiveThreshold(guass, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow('Mean Threshold', thresh)
cv2.waitKey(0)
# Using Gaussian Method
thresh = cv2.adaptiveThreshold(guass, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow('Guassian Threshold', thresh)
cv2.waitKey(0)

# Now Let's Apply Otsu's method
T = mahotas.thresholding.otsu(guass)
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('OTSU', thresh)
cv2.waitKey(0)

# Finally Let's Apply Riddler-Calvard method
T = mahotas.thresholding.rc(guass)
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('Riddler Calvard', thresh)
cv2.waitKey(0)
