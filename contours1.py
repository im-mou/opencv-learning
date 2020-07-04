import cv2 as cv
import numpy as np


img = cv.imread('images/messi5.jpg', -1)
imgg = cv.imread('images/messi5.jpg', 0)
out = np.zeros((512, 512, 3))


ret, th = cv.threshold(imgg, 127, 255, cv.THRESH_BINARY)

cont, hierarchy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(out, cont, -1, (0, 255, 255), 1, hierarchy=hierarchy)

cv.imshow('image', out)
cv.waitKey(0)
cv.destroyAllWindows()
