# Import Required Packages
import cv2
import numpy as np
import mahotas

# Create a variable containing the path to the image
image_path = 'appels.jpg'

# Read the image from the Disk
image = cv2.imread(image_path)
image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow('Blurred Image', blurred)
cv2.waitKey(0)

# Now Let's Apply the Canny Edge Detector
canny = cv2.Canny(blurred, 30, 120)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

# Getting the Contours
(cnts, _) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, cnts, -1, (255, 0, 0), 2)
cv2.imshow('Contours', image)
cv2.waitKey(0)

for i , c in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    appel = image[y:y+h, x:x+w]
    cv2.imshow('Appel', appel)
    cv2.waitKey(0)
    mask = np.zeros(image.shape[0:2], dtype='uint8')
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]
    cv2.imshow('Masked Appel', cv2.bitwise_and(appel, appel, mask=mask))
    cv2.waitKey(0)
