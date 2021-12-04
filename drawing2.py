# Import Required Packages
import cv2
import numpy as np

# Define the Canvas inside which we will draw
canvas = 255 * np.ones((300, 300, 3), dtype='uint8')

# Now Let's Draw

for i in range(0, 25):
    r = np.random.randint(0, 200)
    pt = np.random.randint(0, 200, size=(2,))
    cl = np.random.randint(0, 256, size=(3,)).tolist()
    cv2.circle(canvas, tuple(pt), r, cl, -1)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
