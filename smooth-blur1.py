import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# create kernel => k = kMatrix / (k_h * k_w)
kernel = np.ones((5, 5), np.float32)/25

# filter "D -> homogeneous"
dst = cv.filter2D(img, -1, kernel)

# low pass -> removes noise and blurs the image
# high pass -> helps find images in the image

# blur = 2dFilter = averaging
blur = cv.blur(img, (5, 5))

# gaussion filter -> weights in the center of the kernal are higher than 
# the ones away from the kernel
gblur = cv.GaussianBlur(img, (5, 5), 0)

# median blur -> get the median of the neighbours pixels values
mblur = cv.medianBlur(img, 5)

# bilateral filter -> edges are preserved better
bilat = cv.bilateralFilter(img, 9, 75, 75)

# matlibplot windows titles
titles = ["Original", "2D Convolution", "Blur", "Gaussian", "Median", "BiLat"]
images = [img, dst, blur, gblur, mblur, bilat]

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i]) 
    plt.xticks([]), plt.yticks([])

plt.show()
