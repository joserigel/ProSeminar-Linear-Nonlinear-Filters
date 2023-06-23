import cv2 as cv
import numpy as np
from scipy import ndimage


img = cv.imread("test.jpg")
img = cv.resize(img, (img.shape[1]//20, img.shape[0]//20))
img = img[:128, :128, :]

kernel = [
    [ 1/4, -2/4, 1/4],
    [ -2/4, 1/4, -2/4],
    [ 1/4, -2/4, 1/4]
]
kernel = np.array(kernel).reshape((3, 3, 1))
print(kernel)
img = ndimage.convolve(img, kernel)

cv.imshow('test', img)
cv.waitKey(10000)