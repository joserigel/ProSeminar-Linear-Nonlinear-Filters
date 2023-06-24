import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("triangle.png")


dim = (img.shape[1] * 2 , img.shape[0] * 2)
img = cv.resize(img, dim, interpolation=cv.INTER_NEAREST)
    

img = cv.boxFilter(img, -1, (23, 23))

cv.imshow("test", img)
cv.waitKey(1000)