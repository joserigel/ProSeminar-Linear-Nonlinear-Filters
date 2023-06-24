import cv2 as cv
import numpy as np
from scipy import ndimage

# Read
img = cv.imread("pilot.jpg")
img = cv.resize(img, (img.shape[1] // 4, img.shape[0] // 4))

blurred = cv.GaussianBlur(img, (3, 3), sigmaX=2)
edges = cv.Laplacian(blurred, -1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_REFLECT101)
added = cv.add(img, edges)

cv.imwrite('../img/laplacianOriginal.png', img)
cv.imwrite('../img/laplacian.png', edges)
cv.imwrite('../img/laplacianAdded.png', added)

