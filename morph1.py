import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('smarties.png', 0)

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

# create kernel white
kernel = np.ones((3, 3), np.uint8)

dilation = cv.dilate(mask, kernel, iterations=2)
erosion = cv.erode(mask, kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=2)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=3)
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel, iterations=1)
hit_miss = cv.morphologyEx(mask, cv.MORPH_HITMISS, kernel, iterations=1)
top_hat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel, iterations=5)
black_hat = cv.morphologyEx(mask, cv.MORPH_BLACKHAT, kernel, iterations=5)

#matlibplot windows titles
titles = ["Original", "mask", "Dilation", "Erosion", "Opening", "Closing", "Gradient", "HitMiss", "Top Hat", "Black Hat"]
images = [img, mask, dilation, erosion, opening, closing, gradient, hit_miss, top_hat, black_hat]

for i in range(len(titles)):
    plt.subplot(4, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
