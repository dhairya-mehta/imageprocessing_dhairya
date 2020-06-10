import cv2
import numpy as np
path=r"C:\Users\DHAIRYA MEHTA\Desktop/flower.jpg"
img=cv2.imread(path)
img_height=int(img.shape[0]/7)
img_width=int(img.shape[1]/7)
row_no=0
for j in range(0,7):
    if(j%2==0):
        for i in range(0,7):
            b=np.random.randint(0,255)
            g=np.random.randint(0,255)
            r=np.random.randint(0,255)
            img_1=cv2.rectangle(img,(i*img_width,j*img_height),((i+1)*img_width,(j+1)*img_height),(b,g,r),-1)
            cv2.imshow("frame",img_1)
            cv2.waitKey(500)
    else:
        for i in range(0,7):
            b=np.random.randint(0,255)
            g=np.random.randint(0,255)
            r=np.random.randint(0,255)
            img_1=cv2.rectangle(img,((7-i-1)*img_width,(j)*img_height),((7-i)*img_width,(j+1)*img_height),(b,g,r),-1)
            cv2.imshow("frame",img_1)
            cv2.waitKey(500)
    j+=1