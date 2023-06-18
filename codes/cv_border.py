import cv2 as cv

# Read
img = cv.imread("test.jpg")
img = cv.resize(img, (img.shape[1]//20, img.shape[0]//20))
img = img[:128, :128, :]

types = (cv.BORDER_CONSTANT, cv.BORDER_WRAP, cv.BORDER_REPLICATE, cv.BORDER_REFLECT)
names = ("constant", "wrap", "clamp", "reflect")
for i in range(len(types)):
    bordered = cv.copyMakeBorder(img, 32, 32, 32, 32, types[i])
    dim = (bordered.shape[1] * 4 , bordered.shape[0] * 4)
    bordered = cv.resize(bordered, dim, interpolation=cv.INTER_NEAREST)
    cv.imwrite(f"../img/border_%s.jpg" % names[i], bordered)


