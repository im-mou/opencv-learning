import cv2 as cv

img = cv.imread('lena.jpg', -1)

cv.imshow('image', img)
k = cv.waitKey(0) & 0xFF

if k == 27: # ESC
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('lena_copy.png', img)
    cv.destroyAllWindows()
    