import cv2 as cv
import numpy as np

img = cv.imread('images/gradient.png', 0)

# binary threshold -> either 0 if blow min value and max value if above min
_, th_binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# inverse binary threshold
_, th_binary_inv = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)



# trunc threshold -> apply min value after the min value in image
_, th_trunc = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)


# To Zero threshold -> if pixel val < min then img val=0
_, th_to_zero = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# To Zero inverse threshold
_, th_to_zero_inv = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow('image', img)
cv.imshow('Threshold', th_to_zero_inv)

cv.waitKey(0) 
cv.destroyAllWindows()
    