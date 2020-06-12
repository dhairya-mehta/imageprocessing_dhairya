import cv2
import numpy as np
x_start, y_start, x_end, y_end = 0, 0, 0, 0
def mouse(event,x,y,flags,param):
    flag=0
    global x_start, y_start, x_end, y_end
    if event==cv2.EVENT_LBUTTONDOWN:
        flag=1
        x_start,y_start=x,y
        print(x_start,y_start)
    elif event==cv2.EVENT_RBUTTONDOWN:
        flag=2
        x_end,y_end=x,y
        print(x_end,y_end)
    if flag==2:
        cropped=img[y_start:y_end, x_start:x_end]
        cv2.imshow("crop",cropped)


cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)

path=r"C:\Users\DHAIRYA MEHTA\Desktop\Image Processing\imageprocessing_dhairya\Assignment_4/flower.jpg"
img=cv2.imread(path)
cv2.imshow("frame",img)

cv2.waitKey(0)
