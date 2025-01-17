import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/gradient.png', 0)

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


#matlibplot windows titles
titles = ["Original", "Binary", "Binary_INV", "Trunc", "ToZero", "ToZero_INV"]
images = [img, th1, th2, th3, th4, th5]

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
