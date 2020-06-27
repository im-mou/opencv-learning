import cv2 as cv
import numpy as np

def tb_cb(x):
    print(x)

#img = cv.imread('lena.jpg', -1)
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, tb_cb)
cv.createTrackbar('G', 'image', 0, 255, tb_cb)
cv.createTrackbar('R', 'image', 0, 255, tb_cb)

switch = '0 : OFF\n 1: ON'
cv.createTrackbar(switch, 'image', 0, 1, tb_cb)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if not s:
        img[:] = 0
    else:
        img[:] = [b, g, r]

    
cv.destroyAllWindows()
