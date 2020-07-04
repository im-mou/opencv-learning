import cv2 as cv

img = cv.imread('images/lena.jpg')


# gaussian pyramid

# pyramid down
gp_d1 = cv.pyrDown(img)
gp_d2 = cv.pyrDown(gp_d1)

# pyramid up
gp_u1 = cv.pyrUp(gp_d2)


cv.imshow('Original', img)
cv.imshow('gaussian P. down: 1', gp_d1)
cv.imshow('gaussian P. down: 2', gp_d2)
cv.imshow('gaussian P. up: 1', gp_u1)


cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
    