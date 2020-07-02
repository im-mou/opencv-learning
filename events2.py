import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 3, (255, 0, 0), -1)
        points.append((x, y))
        if len(points) >= 2: 
            cv.line(img, points[-1], points[-2], (0, 255, 0), 2)
        cv.imshow('image', img)

# img = np.zeros([512, 513, 3], dtype=np.uint8)
img = cv.imread('images/lena.jpg', 1)
cv.imshow('image', img)
points = []
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
