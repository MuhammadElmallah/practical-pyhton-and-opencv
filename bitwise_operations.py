# Import the Required Packages
import cv2
import numpy as np

rectangel = np.zeros((300, 300), dtype='uint8')
cv2.rectangle(rectangel, (25, 25), (275, 275), 255, -1)
cv2.imshow('Rectangle', rectangel)
cv2.waitKey(0)

circle = np.zeros((300, 300), dtype='uint8')
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow('Circle', circle)
cv2.waitKey(0)

And = cv2.bitwise_and(rectangel, circle)
cv2.imshow('AND', And)
cv2.waitKey(0)

Or = cv2.bitwise_or(rectangel, circle)
cv2.imshow('OR', Or)
cv2.waitKey(0)

Xor = cv2.bitwise_xor(rectangel, circle)
cv2.imshow('XOR', Xor)
cv2.waitKey(0)

Not = cv2.bitwise_not(rectangel)
cv2.imshow('NOT', Not)
cv2.waitKey(0)
