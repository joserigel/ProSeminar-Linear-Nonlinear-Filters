import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("test.jpg")
img = cv.resize(img, (img.shape[1] // 4, img.shape[0] // 4))

img = img[500:-100, :400]

blurred = cv.GaussianBlur(img, (53, 53), sigmaX=7)
difference = cv.subtract(img, blurred)
sharpened = cv.add(img, difference)

cv.imwrite('../img/original_mask.jpg', img)
cv.imwrite('../img/unsharp_mask.jpg', blurred)
cv.imwrite('../img/difference_unsharp.jpg', difference)
cv.imwrite('../img/sharpened.jpg', sharpened)

