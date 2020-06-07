import cv2 
cap = cv2.VideoCapture(0)
count =0
n = int(input("Enter the no of frame"))
while True :
    count += 1
    x , frame = cap.read()
    flipped = cv2.flip(frame,-1)
    if ((count%n)!=0) :
        cv2.imshow("Image",frame)
    else :
        cv2 .imshow("Image",flipped) 
    if cv2.waitKey(1000) & 0xFF == ord('q') :
        break