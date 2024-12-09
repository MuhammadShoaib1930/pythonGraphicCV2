import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image1 = cv.imread("girl1.jpg")
image2 = cv.imread("girl2.jpg")
print(image1.shape)
exit()
image1_resize = cv.resize(image1,(300,300))
image2_resize = cv.resize(image2,(300,300))

image1_resize_gray = cv.cvtColor(image1_resize,cv.COLOR_BGR2GRAY)
image2_resize_gray = cv.cvtColor(image2_resize,cv.COLOR_BGR2GRAY)

image1_resize_gray_canny = cv.Canny(image1_resize_gray, 100,256)
image2_resize_gray_canny = cv.Canny(image2_resize_gray, 100,256)

_, image1_resize_gray_threshold = cv.threshold(image1_resize_gray,100,256,cv.THRESH_BINARY)
_,image2_resize_gray_threshold = cv.threshold(image2_resize_gray,100,256,cv.THRESH_BINARY)

image1_size = image1_resize_gray.size
image2_size = image2_resize_gray.size

image1_shap = image1_resize_gray.shape
image2_shap = image2_resize_gray.shape

image1_line = cv.line(image1_resize,(50,50),(100,150),(255,0,0))
image2_line = cv.line(image2_resize,(50,50),(100,100),(255,0,0))

image1_rectangle = cv.rectangle(image1_resize,(50,50),(100,150),(0,255,0))
image2_rectangle = cv.rectangle(image2_resize,(50,50),(100,150),(0,256,0))

image1_circle = cv.circle(image1_resize,(50,50),30,(0,0,256))
image2_circle = cv.circle(image2_resize,(50,50),35,(0,0,256))

new_white = np.ones((300,300,3),np.uint8)*255
new_black = np.zeros((300,300,3),np.uint8)

image1_resize_crup = image1_resize
image1_resize_crup = image1_resize[50:200,20:220]
image1_resize_crup[0:150,0:200]=image1_resize_crup

image2_resize_crup = image2_resize
image2_resize_crup = image2_resize_crup[100:200,50:200]
image2_resize_crup[0:100,00:150] = image2_resize_crup

image1_histGram = cv.calcHist([image1_resize_gray],[0],None,[256],[0,256])
image2_histGram = cv.calcHist([image2_resize_gray],[0],None,[256],[0,256])

DefreanceBothImage = abs(image1_resize-image1_resize)

def myFunction(frameName='frameName' ,wait = 1 ):
    opensVideoFrame = cv.VideoCapture(0)
    while opensVideoFrame.isOpened:
        isFrame , frame = opensVideoFrame.read()
        cv.imshow(frameName,frame)
        print(isFrame)
        s = cv.waitKey(wait)
        if s == ord('q') or isFrame == False:
            break
    cv.destroyAllWindows()
myFunction(frameName="shoaib",wait=1)
cv.waitKey(0)
cv.destroyAllWindows()