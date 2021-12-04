# Import Required Packages
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)

# Now Let's Calculate the Histogram
# Gray Scale Histogram
Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', Gray)
cv2.waitKey(0)
hist = cv2.calcHist([Gray], [0], None, [256], [0, 256])

# Visualizing The Grayscale Histogram
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

# Visualizing The Color Histogram
cv2.imshow('Colored Image', image)
cv2.waitKey(0)
chans = cv2.split(image)
colors = ('b', 'g', 'r')
plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
for chan, color in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

# Visualizing 2D Histograms
figure = plt.figure()
ax = figure.add_subplot(131)
hist = cv2.calcHist([chans[0], chans[1]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation='nearest')
ax.set_title('Blue ang Green Channels')
plt.colorbar(p)

ax = figure.add_subplot(132)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation='nearest')
ax.set_title('Blue and Red Channels')
plt.colorbar(p)

ax = figure.add_subplot(133)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation='nearest')
ax.set_title('Green and Red Channels')
plt.colorbar(p)
plt.show()
cv2.waitKey(0)

# Histogram Equalization (Applied to Grayscale Images)
eq = cv2.equalizeHist(Gray)
cv2.imshow('Histogram Equalization', np.hstack([Gray, eq]))
cv2.waitKey(0)
hist = cv2.calcHist([eq], [0], None, [256], [0, 256])
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)


