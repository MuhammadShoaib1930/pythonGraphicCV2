
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("football2.jpg")
img= cv.resize(img,(500,500))

ts = img[230:350,160:230]
img[350:350+350-230,330:330+230-160] = ts

cv.imshow("s",img)
plt.imshow(img)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Image")
w,h,channel = img.shape
plt.xticks(np.arange(0, w, step=60))
plt.yticks(np.arange(0, h, step=60))
img2 = img[80:80,140:120]
print(img.shape)
# cv.imshow("this",img2)
plt.axis('on')  
plt.grid(True) 
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()