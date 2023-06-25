import cv2 as cv
import numpy as np
from scipy import ndimage


img = cv.imread("color.jpg")
kernel = np.array([[[0, 0, 1]]])
convolved = ndimage.convolve(img, kernel, mode='reflect')
cv.imwrite('../img/colorShift.jpg', convolved)