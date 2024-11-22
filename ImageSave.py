import cv2 as cv

img = cv.imread("image1.jpg") # Read image and store it variable

if img is None: # if image is not Present then do that
    print("The image is not found") # to Print the image is not present 
    exit() # To close the execution 

cv.imshow("Display",img) # To show / open the image in window
k = cv.waitKey(0)
if k == "s": # If the user press s then save the image
    cv.imwrite("output.jpg",img) # to save the image 
else: # if the user press q then close the execution
    cv.destroyAllWindows() # close all execution of running
