import cv2 as cv
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = cv.imread("lena.jpg")
img2 = cv.resize(img2, (500, 250))


# bitwise and
b_and = cv.bitwise_and(img1, img2)


#bit_or
b_or = cv.bitwise_or(img1, img2)


#bit_xor
b_xor = cv.bitwise_xor(img1, img2)


#bit_not
b_not = cv.bitwise_not(img2)


cv.imshow("image 1", img1)
cv.imshow("image 2", img2)
cv.imshow("image bit_not", b_xor)

cv.waitKey(0)
cv.destroyAllWindows()
