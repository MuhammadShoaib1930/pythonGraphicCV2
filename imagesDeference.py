import numpy as np
import cv2 as cv

img1 = cv.imread("apple1.png",0)
img1_resize_canny = cv.resize(img1,(300,320))
img1_canny = cv.Canny(img1_resize_canny,200,255)
cv.imshow('ss',img1_canny)
img2 = cv.imread("apple2.jpg",0)
img2_resize_canny = cv.resize(img2,(300,320))
img2_canny = cv.Canny(img2_resize_canny,200,255)

image1_array = np.array(img1_resize_canny)
image2_array = np.array(img2_resize_canny)
deference_matrix = abs(image1_array-image2_array)

deference_image = cv.normalize(src=deference_matrix,dst= None,alpha= 0,beta= 255,norm_type= cv.NORM_MINMAX)
imagesShow = np.hstack((img1_canny,img2_canny , deference_image))
cv.imshow("img 1 , img 2 , deference ",imagesShow)

cv.waitKey(0)
cv.destroyAllWindows()