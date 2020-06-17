import cv2
import numpy as np 
img=cv2.imread(r"C:\Users\DHAIRYA MEHTA\Desktop\Image Processing\imageprocessing_dhairya\Assignment_6\edge_detection.jpg")
s=25
width=int(img.shape[1]*s/100)
height=int(img.shape[0]*s/100)
dim=(width,height)
img=cv2.resize(img,dim)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussian_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,2)


gaussian_kernel = np.array([1,2,1,
                            2,4,2,
                            1,2,1 ])/16

gaussian_blur = cv2.filter2D(gaussian_thresh,-1,gaussian_kernel)
gaussian_blur = cv2.GaussianBlur(img_gray,(25,25),2)

kernel_2 = np.ones((5,5))

opening_processed = cv2.morphologyEx(gaussian_blur,cv2.MORPH_OPEN,kernel_2)
closing_processed = cv2.morphologyEx(opening_processed,cv2.MORPH_CLOSE,kernel_2)

canny = cv2.Canny(closing_processed,12,50)
cv2.imshow('Canny',canny)
cv2.waitKey(0)