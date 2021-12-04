import cv2
import numpy as np

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image, angel, center=None, scale=1):
    (h, w) = image.shape[0:2]
    if center == None:
        center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angel, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def resize(image, height=0, width=0, inter=cv2.INTER_AREA):
    if height != 0 and width == 0:
        r = height / image.shape[0]
        dim = (height, int(r * image.shape[1]))
        resized = cv2.resize(image, dim, inter)
    elif width != 0 and height == 0:
        r = width / image.shape[1]
        dim = (int(r * image.shape[0]), width)
        resized = cv2.resize(image, dim, inter)
    elif width == 0 and height == 0:
        return image
    else:
        dim = (height, width)
        resized = cv2.resize(image, dim, inter)

    return resized



