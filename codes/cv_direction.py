import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("pattern.png")
img = cv.GaussianBlur(img, ksize=(7,7), sigmaX=5)

sobel = ndimage.sobel(img, axis=1)
prewitt = ndimage.prewitt(img, axis=1)



cv.imwrite("../img/directionPattern.png", img)
cv.imwrite("../img/directionSobel.png", sobel)
cv.imwrite("../img/directionPrewitt.png", prewitt)


