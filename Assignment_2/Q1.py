import cv2
path=r"C:\Users\DHAIRYA MEHTA\Desktop\Image Processing\imageprocessing_dhairya\Assignment_2/flower.jpg"
img=cv2.imread(path)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),5)
cv2.imshow("frame",img)
cv2.waitKey(0)
