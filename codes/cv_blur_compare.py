import cv2 as cv

# Read
img = cv.imread("ellipse.png")

gaussian = cv.GaussianBlur(img, (233, 233), sigmaX=53, borderType=cv.BORDER_CONSTANT)
bilinear = cv.bilateralFilter(img, -1, )
box = cv.boxFilter(img, -1, (133, 133), borderType=cv.BORDER_CONSTANT)


cv.imwrite("../img/blurGaussian.png", gaussian[70:-70, :])
cv.imwrite("../img/blurBox.png", box[70:-70, :])


