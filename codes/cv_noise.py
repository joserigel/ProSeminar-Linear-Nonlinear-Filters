import cv2 as cv

# Read
img = cv.imread("noise.jpg")

gaussian = cv.GaussianBlur(img, (27, 27), sigmaX=7, borderType=cv.BORDER_REFLECT)

difference = cv.subtract(img, gaussian)
difference = cv.subtract(img, difference)

cv.imwrite("../img/noiseSuppressed.jpg", gaussian)
cv.imwrite("../img/noiseEnhanced.jpg", difference)

