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
# Now Let's Creat the Mask
mask = np.zeros(image.shape[0:2], dtype='uint8')
(cx, cy) = (image.shape[1] // 2, image.shape[1] // 2)
cv2.rectangle(mask, (cx - 75, cy - 75), (cx + 75, cy + 75), 255, -1)
cv2.imshow('Mask', mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Masked', masked)
cv2.waitKey(0)

mask2 = np.zeros(image.shape[0:2], dtype='uint8')
cv2.circle(mask2, (cx, cy), 100, 255, -1)
cv2.imshow('Mask2', mask2)
cv2.waitKey(0)

masked2 = cv2.bitwise_and(image, image, mask=mask2)
cv2.imshow('Masked2', masked2)
cv2.waitKey(0)
