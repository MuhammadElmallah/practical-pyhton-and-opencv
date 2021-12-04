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
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# Now Let's Calculate the Gradient using the Laplacian function
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute((lap)))
cv2.imshow('Laplacian', lap)
cv2.waitKey(0)

# Now Let's Compute the Sobel Gradient
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelx = np.uint8(np.absolute(sobelx))
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)

sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sobely = np.uint8(np.absolute((sobely)))
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)

sobelCombined = cv2.bitwise_or(sobely, sobely)
cv2.imshow('Sobel Combined', sobelCombined)
cv2.waitKey(0)
