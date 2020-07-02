import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        b = img[x, y, 0]
        g = img[x, y, 1]
        r = img[x, y, 2]

        cv.circle(img, (x, y), 3, (0, 0, 225), -1)
        cimg = np.zeros((512, 512, 3), np.uint8)

        cimg[:] = [b, g, r]

        cv.imshow('colorWindow', cimg)

# img = np.zeros([512, 513, 3], dtype=np.uint8)
img = cv.imread('images/lena.jpg', 1)
cv.imshow('image', img)
points = []
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
