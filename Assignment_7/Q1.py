import cv2
import numpy as np 

def nothing(x):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow('Colorbars') 
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd = 'Colorbars'

cv2.createTrackbar(hl, wnd,0,179,nothing)
cv2.createTrackbar(hh, wnd,0,179,nothing)
cv2.createTrackbar(sl, wnd,0,255,nothing)
cv2.createTrackbar(sh, wnd,0,255,nothing)
cv2.createTrackbar(vl, wnd,0,255,nothing)
cv2.createTrackbar(vh, wnd,0,255,nothing)

while True:
    x,frame=cap.read()
    frame=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hul=cv2.getTrackbarPos(hl, wnd)
    huh=cv2.getTrackbarPos(hh, wnd)
    sal=cv2.getTrackbarPos(sl, wnd)
    sah=cv2.getTrackbarPos(sh, wnd)
    val=cv2.getTrackbarPos(vl, wnd)
    vah=cv2.getTrackbarPos(vh, wnd)
    HSVLOW=np.array([hul,sal,val])
    HSVHIGH=np.array([huh,sah,vah])
    mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
    res = cv2.bitwise_and(frame,frame, mask =mask) 
    cv2.imshow(wnd, res)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

