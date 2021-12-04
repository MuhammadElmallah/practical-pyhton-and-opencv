# Import Required Packages
import cv2
import numpy as np

# Define the Canvas inside which we will draw
canvas = 255 * np.ones((300, 300, 3), dtype='uint8')
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

# Now let's Draw
green = (0, 255, 0)
red = (0, 0, 255)

cv2.circle(canvas, (150, 150), 0, green, 100)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.circle(canvas, (150, 150), 50, red, 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.circle(canvas, (150, 150), 75, (255, 0, 0), 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.circle(canvas, (150, 150), 100, (255, 255, 0), 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (25, 25), (275, 275), red, 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (0, 0), (300, 300), green, 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.line(canvas, (0, 0), (300, 300), green, 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)

cv2.line(canvas, (0, 300), (300, 0), red, 15)
cv2.imshow('Updated Canvas', canvas)
cv2.waitKey(0)
