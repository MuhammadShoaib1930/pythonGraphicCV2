import numpy as np
import cv2 as cv

image = cv.imread('apple1.png', 0)
image  =cv.resize(image,(500,500))
_, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
binary_image = binary_image/255
print(binary_image)
cv.imshow("binary",binary_image)
cv.waitKey(0)
cv.destroyAllWindows()