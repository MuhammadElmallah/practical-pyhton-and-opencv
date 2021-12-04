# Import Required Packages
import cv2
import numpy as np

# Define the Canvas inside which we will draw
canvas = 255 * np.ones((300, 300, 3), dtype='uint8')
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# Now let's Draw our Rectangles
green = (0, 255, 0)
red = (0, 0, 255)

cv2.rectangle(canvas, (0, 0), (300, 300), green, 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (25, 25), (275, 275), red, 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 50), (250, 250), (255, 0, 0), 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (75, 75), (225, 225), (255, 255, 0), -15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

