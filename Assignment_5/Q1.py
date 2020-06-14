import cv2
import numpy as np

cap=cv2.VideoCapture(0)

points=[]
def mouse(event,x,y,flags,param):
    f=False
    if event==cv2.EVENT_LBUTTONDOWN:
        if f == False:
            f=True
            cv2.imwrite('template.jpg',frame)     
        points.append((x,y))

while True:
    x,frame=cap.read()
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',mouse)
    img=cv2.imread('template.jpg')
    if len(points)==2:
        img_cropped=img[points[0][1]:points[1][1],points[0][0]:points[1][0]]
        cv2.imshow('cropped',img_cropped)
        template_gray=cv2.cvtColor(img_cropped,cv2.COLOR_BGR2GRAY)
        width=img_cropped.shape[1]
        height=img_cropped.shape[0]
        img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        res=cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED)
        loc=np.where(res>=0.7)

        for x,y in zip(*loc[::-1]):
            cv2.rectangle(frame,(x,y),(x+height,y+width),(0,255,0),1)
            cv2.putText(frame,'OBJECT',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break