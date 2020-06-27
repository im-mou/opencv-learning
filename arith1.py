import cv2 as cv
import numpy as np


img = cv.imread('lena.jpg')
img2 = cv.imread('opencv-logo-white.png')

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv.split(img)
img = cv.merge((g, b, r))

# ROI - reigon of interest
area = img[280:340, 330:390]
img[273:333, 100:160] = area

# resize the second image
img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))

# add two images
#dst = cv.add(img, img2)

# add tow images with diferents dominance level
dst = cv.addWeighted(img, 0.9, img2, 0.1, 0)


cv.imshow('image', dst)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()