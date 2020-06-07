from cv2 import cv2
import time
start=time.time()
cap=cv2.VideoCapture(0)
while True:
    end=time.time()
    time_diff=int(end-start)
    x,img=cap.read()
    flip=cv2.flip(img,-1)
    if(time_diff%5==0):
        cv2.imshow("image",flip)
    else:
        cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break