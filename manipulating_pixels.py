# Import Required Packages
import cv2

# Create a variable containing the path to the image
image_path = 'homeImage.jpeg'

# Read the image from the Disk
image = cv2.imread(image_path)

# Display the Original Image on the Screen
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Now Let's get access to a specific pixel in the image
(b, g, r) = image[0, 0]
print('The value of the Red channel of Pixel (0, 0) is: ', r)
print('The value of the Green channel of Pixel (0, 0) is: ', g)
print('The value of the Blue channel of Pixel (0, 0) is: ', b)

print('*****-----*****-----*****-----*****-----*****-----')

# Now Let's manipulate this Pixel
image[0, 0] = (0, 255, 0)
cv2.imshow('Manipulated Image', image)
cv2.waitKey(0)
(b, g, r) = image[0, 0]
print('The value of the Red channel of Pixel (0, 0) is: ', r)
print('The value of the Green channel of Pixel (0, 0) is: ', g)
print('The value of the Blue channel of Pixel (0, 0) is: ', b)

# Accessing a bigger portion of an Image
corner = image[0:100, 0:100]
cv2.imshow('Portion of the Image', corner)
cv2.waitKey(0)

# Manipulating this Portion of the Image
image[0:50, 0:100] = (0, 0, 255)
cv2.imshow('Updated Image', image)
cv2.waitKey(0)

