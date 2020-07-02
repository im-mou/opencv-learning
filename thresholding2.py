import cv2 as cv
import numpy as np

def tb_cb(x):
    pass

img = cv.imread('images/sudoku.png', 0)

cv.namedWindow('params')
cv.createTrackbar('maxValue', 'params', 255, 255, tb_cb)
cv.createTrackbar('blockSize', 'params', 11, 256, tb_cb)
cv.createTrackbar('constant', 'params', 0, 512, tb_cb)


while True:

    _mv = cv.getTrackbarPos('maxValue', 'params')
    _bs = cv.getTrackbarPos('blockSize', 'params')
    _c = cv.getTrackbarPos('constant', 'params')

    if _bs % 2 == 0:
        _bs = _bs + 1

    adoptive_thresh_mean = cv.adaptiveThreshold(img, _mv, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, _bs, _c)
    adoptive_thresh_gaussian = cv.adaptiveThreshold(img, _mv, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, _bs, _c)

    #cv.imshow('image', img)
    cv.imshow('Threshold Mean', adoptive_thresh_mean)
    cv.imshow('Threshold Gausian', adoptive_thresh_gaussian)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
    