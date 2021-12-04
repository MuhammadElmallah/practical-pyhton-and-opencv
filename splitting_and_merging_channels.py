# Import Required Packages
import cv2
import numpy as np

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)
image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)
cv2.imshow('Image', image)
cv2.waitKey(0)

# Now Let's Play with the Channels, Splitting and Merging

(B, G, R) = cv2.split(image)
cv2.imshow('RED', R)
cv2.waitKey(0)
cv2.imshow('GREEN', G)
cv2.waitKey(0)
cv2.imshow('BLUE', B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow('Merged', merged)
cv2.waitKey(0)

zeros = np.zeros(image.shape[0:2], dtype='uint8')
cv2.imshow('Red Channel', cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
cv2.imshow('Green Channel', cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.imshow('Blue Channel', cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
