import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("test.jpg")
img = cv.resize(img, (img.shape[1]//20, img.shape[0]//20))
img = img[:128, :128, :]

#img = cv.copyMakeBorder(img, 16, 16, 16, 16, cv.BORDER_REFLECT)

# size = 13
# kernel = np.full((size, size, 1), 0.0)
# kernel[:, :, 0] = 1 / (size * size)

# img = ndimage.convolve(img, kernel, mode='constant', cval=255)
dim = (img.shape[1] * 4 , img.shape[0] * 4)
img = cv.resize(img, dim, interpolation=cv.INTER_NEAREST)

types = (cv.BORDER_CONSTANT, cv.BORDER_WRAP, cv.BORDER_REPLICATE, cv.BORDER_REFLECT)
for i in types:
    bordered = cv.copyMakeBorder(img, 32, 32, 32, 32, i)
    cv.imwrite("border_"+str(i)+".jpg", bordered)

# while (True):
#     cv.imshow("title", img)
#     if (cv.waitKey(0)):
#         break
