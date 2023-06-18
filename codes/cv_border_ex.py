import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("test.jpg")
img = cv.resize(img, (img.shape[1]//20, img.shape[0]//20))
img = img[:128, :128, :]

size = 17
kernel = np.full((size, size, 1), 0.0)
kernel[:, :, 0] = 1 / (size * size)

types = ("constant", "wrap", "nearest", "mirror")
names = ("constant", "wrap", "clamp", "reflect")
for i in range(len(types)):
    bordered = ndimage.convolve(img, kernel, mode=types[i])
    dim = (bordered.shape[1] * 4 , bordered.shape[0] * 4)
    bordered = cv.resize(bordered, dim, interpolation=cv.INTER_NEAREST)
    cv.imwrite(f"../img/boxBlur_%s.jpg" % names[i], bordered)


