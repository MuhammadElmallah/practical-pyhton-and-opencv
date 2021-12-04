#import the required libraries
import cv2

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)

print('The Height of the image is: ', image.shape[0])
print('The Width of the image is: ', image.shape[1])
print('The Number of the Channels in the image is: ', image.shape[2])
print('Image Dimensions are: ', image.shape)
print('Image Variable Type is: ', type(image))

# Displaying the Image on the Screen
cv2.imshow('image', image)

#Pause the execution of the script until we press a key on our keyboard
cv2.waitKey(0)          # Using a parameter of (0) indicates that any keypress will un-pause the execution

# Write the image file in JPG format
cv2.imwrite('image.jpg', image)


