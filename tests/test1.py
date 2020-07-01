import os
import sys
import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv.imread('../pca_test1.jpg', 0)

gaussian = cv.GaussianBlur(img, (3, 3), 0)

sobelX = cv.Sobel(gaussian, cv.CV_64F, 1, 0)
#sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv.Sobel(gaussian, cv.CV_64F, 0, 1)
# sobelY = np.uint8(np.absolute(sobelY))

# sobelX = np.where(sobelX > 5, sobelX, 0)
# sobelY = np.where(sobelY > 5, sobelY, 0)


#  calculate arct tan and transform form radians to degrees
gradient = 180 + np.arctan(sobelY / sobelX) / math.pi * 180

# cast to int and remove nan values
gradient = np.uint8(np.nan_to_num(gradient))

h, w = img.shape
new_img = np.zeros((h, w, 3), np.uint8)

new_img[:] = [0, 255, 255]
new_img[:, :, 0] = gradient
new_img[:, :, 2] = np.where(gradient > 0, 255, 0)

new_img = cv.cvtColor(new_img, cv.COLOR_HSV2RGB)


title = ["Image", "Gradient", "Sobel"]
images = [img, new_img, gradient ]


for i in range(len(title)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
