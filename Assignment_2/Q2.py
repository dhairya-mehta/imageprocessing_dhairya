from cv2 import cv2
import os
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
count =55
n = int(input("Enter the no of images "))
while True:
    x , frame = cap.read()
    cv2.imshow("image",frame)
    if(count<=n):   
        x=cv2.imwrite("dataset/IMG_"+str(count)+".jpg",frame)
        print(count)
    count+=1
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

