import cv2
import numpy as np
cap=cv2.VideoCapture(0)
count = 0
while True:
    count+=1
    x,frame=cap.read()
    flip1 = np.rot90(frame)
    flip2=cv2.flip(flip1,-1)
    if(count%2==0):
        cv2.imshow("img",flip1)
    else:
        cv2.imshow("img",flip2)
    if cv2.waitKey(1000) & 0xFF == ord('q') :
        break