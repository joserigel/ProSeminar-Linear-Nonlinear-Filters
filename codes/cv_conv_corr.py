import cv2 as cv
import numpy as np
from scipy import ndimage


img = cv.imread("test.jpg")
img = cv.resize(img, (img.shape[1]//20, img.shape[0]//20))
img = img[:128, :128, :]

size = 32
kernel = np.full((size, size, 1), 0.0)
kernel[0, 0, 0] = 1


dim = (img.shape[1] * 4 , img.shape[0] * 4)

convolved = ndimage.convolve(img, kernel, mode='constant')
convolved = cv.resize(convolved, dim, interpolation=cv.INTER_NEAREST)

correlation = ndimage.correlate(img, kernel, mode='constant')
correlation = cv.resize(correlation, dim, interpolation=cv.INTER_NEAREST)

cv.imwrite('../img/correlation.jpg', correlation)
cv.imwrite('../img/convolved.jpg', convolved)