import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("nasa.jpg")
#img = cv.resize(img, (img.shape[1] // 4, img.shape[0] // 4))

horizontal = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
vertical = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)


cv.imwrite('../img/sobelHorizontal.png', horizontal)
cv.imwrite('../img/sobelVertical.png', vertical)

