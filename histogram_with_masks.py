# Import Required Packages
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)
image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)

def plot_hist(image, title, mask=None):
    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title(title)
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    for chan, color in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)

plot_hist(image, 'Histogram of the Original Image')
mask = np.zeros(image.shape[0:2], dtype='uint8')
cv2.rectangle(mask, (100, 100), (200, 200), 255, -1)
cv2.imshow('Mask', mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Masked Image', masked)
cv2.waitKey(0)

plot_hist(image, 'Historam with Mask', mask=mask)
