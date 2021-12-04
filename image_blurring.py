# Import Required Packages
import cv2
import numpy as np

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)
image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)

# The first blurring method we are going to explore is averaging.
# We are going to define a k × k sliding window on top of our image, where k is always an odd number. (we have to use an odd number, otherwise there would not be a true “center”)
# This window is going to slide from left-to-right and from top-to-bottom.
# The pixel at the center of this matrix  is then set to be the average of all other pixels surrounding it.
# As the size of the kernel increases, the more blurred our image will become.
blurred = np.hstack([image, cv2.blur(image, (3, 3)), cv2.blur(image, (5, 5)), cv2.blur(image, (7, 7)), cv2.blur(image, (9, 9)), cv2.blur(image, (11, 11))])
cv2.imshow('Averged Blurring', blurred)
cv2.waitKey(0)

# Next up, we are going to review Gaussian blurring.
# Gaussian blurring is similar to average blurring, but instead of using a simple mean, we are now using a weighted mean,
# where neighborhood pixels that are closer to the central pixel contribute more “weight” to the average.
guassian_blurred = np.hstack([image, cv2.GaussianBlur(image, (3, 3), 0), cv2.GaussianBlur(image, (5, 5), 0), cv2.GaussianBlur(image, (7, 7), 0), cv2.GaussianBlur(image, (9, 9), 0), cv2.GaussianBlur(image, (11, 11), 0)])
cv2.imshow('Guassian Blurred', guassian_blurred)
cv2.waitKey(0)

# Next up, we will use the Median Blur. When applying a median blur, we first define our kernel size k. Then, as in the averaging blurring method.
# we consider all pixels in the neighborhood of size k × k. But, unlike the averaging method, instead of replacing the central pixel
# with the average of the neighborhood, we instead replace the central pixel with the median of the neighborhood.
median_blurred = np.hstack([image, cv2.medianBlur(image, 3), cv2.medianBlur(image, 5), cv2.medianBlur(image, 7), cv2.medianBlur(image, 9), cv2.medianBlur(image, 11)])
cv2.imshow('Median Blur', median_blurred)
cv2.waitKey(0)

# Finally, we will consider the Bi-lateral Blurring. this method is able to preserve edges of an image, while still reducing noise.
# The largest downside to this method is that it is considerably slower than its averaging, Gaussian, and median blurring counterparts.
bilateral_blurring = np.hstack([image, cv2.bilateralFilter(image, 3, 11, 11), cv2.bilateralFilter(image, 5, 21, 21), cv2.bilateralFilter(image, 7, 31, 31), cv2.bilateralFilter(image, 9, 41, 41), cv2.bilateralFilter(image, 11, 51, 51)])
cv2.imshow('Bi Lateral Blurring', bilateral_blurring)
cv2.waitKey(0)
