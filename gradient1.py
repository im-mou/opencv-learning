import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/sudoku.png', 0)

lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
# cv.CV_64F datatype -> supports the negative slope value
lap = np.uint8(np.absolute(lap))

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_or = cv.bitwise_or(sobelX, sobelY)

#matlibplot windows titles
titles = ["Original", "Laplacian", "SobelX", "SobelY", "Sobel combined"]
images = [img, lap, sobelX, sobelY, sobel_or]

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
 