import cv2 as cv

img = cv.imread('images/lena.jpg')

gp_arr = cv.pyrDown(img)
gaussian_ext = cv.pyrUp(gp_arr)
laplacian = cv.subtract(img, gaussian_ext)

cv.imshow('PyrDown', gp_arr)
cv.imshow('lpacian', laplacian)
cv.waitKey(0)
cv.destroyAllWindows()
