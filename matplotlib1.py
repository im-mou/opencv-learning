import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/lena.jpg', -1)

cv.imshow('image', img)

# matplot displays images in RGB format
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)

# hide axis ticks 
plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()