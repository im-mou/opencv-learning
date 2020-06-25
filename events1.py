import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = str(x) +', '+ str(y)
        cv.putText(img, text, (x, y), font, 0.4, (0, 0, 0), 1, cv.LINE_AA)
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv.FONT_HERSHEY_SIMPLEX
        bgr = str(blue) +', '+ str(green)+', '+ str(red)
        cv.putText(img, bgr, (x, y), font, 0.4, (0, 0, 0), 1, cv.LINE_AA)
        cv.imshow('image', img)


# img = np.zeros([512, 513, 3], dtype=np.uint8)
img = cv.imread('lena.jpg', 1)
cv.imshow('image', img)

cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
