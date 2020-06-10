import cv2
import numpy as np
path=r"C:\Users\DHAIRYA MEHTA\Desktop/flower.jpg"
img=cv2.imread(path)
img_height=int(img.shape[0]/7)
img_width=int(img.shape[1]/7)

for i in range(7):
    for j in range(7):
        b=np.random.randint(0,255)
        g=np.random.randint(0,255)
        r=np.random.randint(0,255)
        img_1=cv2.rectangle(img,(i*img_width,j*img_height),((i+1)*img_width,(j+1)*img_height),(b,g,r),-1)

cv2.imshow("frame",img_1)

cv2.waitKey(0)