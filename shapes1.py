import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg', -1)

# img = np.zeros([512, 512, 3], dtype=np.uint8)

img = cv.line(img, (0, 0), (255, 255), (255, 0, 0), 2)

img = cv.arrowedLine(img, (200, 0), (255, 0), (255, 255, 0), 2)

img = cv.rectangle(img, (0, 0), (300, 300), (255, 255, 0), 2)

img = cv.circle(img, (350, 200), 50, (0, 0, 255), 3)

font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, 'This is a Text', (100, 200), font, 2, (64,246,134), 2, cv.LINE_AA)

cv.imshow('image', img)


k = cv.waitKey(0) & 0xFF
if k == 27: # ESC
    cv.destroyAllWindows()
