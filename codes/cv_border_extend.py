import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("test.jpg")
img = cv.resize(img, (img.shape[1]//20, img.shape[0]//20))
img = img[:128, :128, :]

clamped = cv.copyMakeBorder(img, 32, 32, 32, 32, cv.BORDER_REPLICATE)
mirrored = cv.copyMakeBorder(img, 32, 32, 32, 32, cv.BORDER_REFLECT)
constant = cv.copyMakeBorder(img, 32, 32, 32, 32, cv.BORDER_CONSTANT)

img = cv.subtract(clamped, mirrored)
img = cv.add(constant, img)

size = 17
kernel = np.full((size, size, 1), 0.0)
kernel[:, :, 0] = 1 / (size * size)

blurred = ndimage.convolve(img, kernel, mode='constant')
blurred = blurred[32:-32, 32:-32, :]
blurred = cv.resize(blurred, 
    (blurred.shape[1] * 4 , blurred.shape[0] * 4),
    interpolation=cv.INTER_NEAREST)

img = cv.resize(img,
    (img.shape[1] * 4 , img.shape[0] * 4),
    interpolation=cv.INTER_NEAREST)

cv.imwrite("../img/border_extend.jpg", img)
cv.imwrite("../img/boxBlur_extend.jpg", blurred)
