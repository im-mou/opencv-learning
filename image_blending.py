import cv2 as cv
import numpy as np

apple = cv.imread('images/apple.jpg')
orange = cv.imread('images/orange.jpg')

img = np.hstack((apple[:, :256, :], orange[:, 256:, :]))

# gaussian pyramids apple 
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# gaussian pyramids orange 
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)



# laplacian pyramid apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    g_ext = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], g_ext)
    lp_apple.append(laplacian)


# laplacian pyramid orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    g_ext = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], g_ext)
    lp_orange.append(laplacian)


# join half of images
apple_orange_pyr = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, channels = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyr.append(laplacian)

# reconstruct image
apple_orange_recons = apple_orange_pyr[0]
for i in range(1, 6):
    apple_orange_recons = cv.pyrUp(apple_orange_recons)
    apple_orange_recons = cv.add(apple_orange_pyr[i], apple_orange_recons)


cv.imshow('apple', apple)
cv.imshow('orange', orange)
cv.imshow('half', apple_orange_recons)

cv.waitKey(0)
cv.destroyAllWindows()
