import cv2 as cv

# Read
img = cv.imread("pattern.png")

sobel = cv.Sobel(img, -1, 1, 0)
scharr = cv.Scharr(img, -1, 1, 0)

cv.imwrite("../img/directionPattern.png", img)
cv.imwrite("../img/directionSobel.png", sobel)
cv.imwrite("../img/directionScharr.png", scharr)


