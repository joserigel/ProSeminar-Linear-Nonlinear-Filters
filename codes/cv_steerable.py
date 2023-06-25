import cv2 as cv

# Read
img = cv.imread("pattern2.png")
img = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv.h

cv.imwrite("../img/steerEdge.png", img)


