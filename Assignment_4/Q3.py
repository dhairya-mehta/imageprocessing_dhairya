import cv2
import numpy as np
x1,x2,x3,x4,y1,y2,y3,y4=0,0,0,0,0,0,0,0
def mouse(event,x,y,flags,param):
    flag=0
    global x1,x2,x3,x4,y1,y2,y3,y4
    if event==cv2.EVENT_LBUTTONDOWN:
        flag=1
        x1,y1=x,y
        print(x1,y1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        flag=2
        x2,y2=x,y
        print(x2,y2)
    elif event==cv2.EVENT_LBUTTONUP:
        flag=3
        x3,y3=x,y
        print(x3,y3)
    elif event==cv2.EVENT_RBUTTONUP:
        flag=4
        x4,y4=x,y
        print(x4,y4)
    if flag==4:    
        array1=np.array([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],np.float32)
        array2=np.array([(0,0),(1100,0),(0,1200),(1100,1200)],np.float32)
        perspective=cv2.getPerspectiveTransform(array1,array2)
        transformed=cv2.warpPerspective(img,perspective,(1100,1200))
        cv2.imshow("Image",transformed)



cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)

path=r"C:\Users\DHAIRYA MEHTA\Desktop\Image Processing\imageprocessing_dhairya\Assignment_4/warp.jpg"
img=cv2.imread(path)

cv2.imshow("frame",img)

cv2.waitKey(0)
