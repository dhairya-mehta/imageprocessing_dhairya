import cv2
import numpy as np 
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pytesseract
from PIL import Image
from pytesseract import Output


count=0
root = tk.Tk()
root.title("Optical Character Recognition App")
root.geometry('1000x600')

def auto():
    global transform_auto
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel=np.ones((15,15),dtype=np.float32)/225
    img_gray_filter=cv2.filter2D(img_gray,-1,kernel)
    
    img_gray_smooth = cv2.GaussianBlur(img_gray_filter,(5,5),0)
    canny = cv2.Canny(img_gray_smooth,150, 200)


    contour, hierarchy = cv2.findContours(img_gray_smooth,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    areas = [cv2.contourArea(c) for c in contour]
    max_index = np.argmax(areas)
    maxval_contour = contour[max_index]
    perimeter = cv2.arcLength(maxval_contour, True)
    locations = cv2.approxPolyDP(maxval_contour, 0.01*perimeter, True)
    cv2.drawContours(canny, [locations], -1, (0,0,255), 5)
    x1=np.array([locations[1], locations[0], locations[2], locations[3]],dtype=np.float32)
    x2=np.array([(0,0), (600,0), (0,600) , (600,600)],dtype=np.float32)
    perspective = cv2.getPerspectiveTransform(x1,x2)
    transform_auto = cv2.warpPerspective(img, perspective, (600,600))
    cv2.imshow('Auto crop', transform_auto)
    return(transform_auto)

def manual():
    pts=[]
    def mouse(event,x,y,flags,param):
        
        if event==cv2.EVENT_LBUTTONDOWN:
            pts.append((x,y))
        if len(pts)==4:
            
            pts_1=np.array([pts[0],pts[1],pts[3],pts[2]],np.float32)
            pts_2=np.array([(0,0),(400,0),(0,400),(400,400)],np.float32)
            perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
            cv2.imshow('Manual crop',img)
            transformed_manual=cv2.warpPerspective(img,perspective,(400,400))
            cv2.imshow('New image',transformed_manual)
            if cv2.waitKey(1000) & 0xFF == ord('q') :
                cv2.destroyAllWindows()
    cv2.namedWindow('Manual crop')
    cv2.imshow('Manual crop', img)
    cv2.setMouseCallback('Manual crop',mouse)

def image_open_btn_clicked():
    global img,filename
    filename = filedialog.askopenfilename(title = 'Select the Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    img = cv2.imread(filename)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == 'q':
        cv2.destroyWindow('frame')

def show_txt():
    textbox = tk.Frame(right_frame,bg = '#FDFFD6')
    textbox.place(relx = 0.02,rely = 0.02,relwidth =0.95,relheight =0.95)
    #text = pytesseract.image_to_string(img)
    value=Image.open(filename)
    text = Text(textbox,bg = '#FDFFD6')
    text.insert('1.0',pytesseract.image_to_string(value))
    text.pack()
    
    

def save_image():
    global count
    count+=1
    cv2.imwrite('image_'+str(count) + '.jpg', img_1)


def close_all():
    root.destroy()



def show_ocr():
    global img_1
    data = pytesseract.image_to_data(img,output_type= Output.DICT)
    no_word = len(data['text'])
    img_1=img.copy()
    for i in range(no_word):
        if int(data['conf'][i]) > 90:
            x,y,w,h = data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(img_1,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.imshow('frame',img_1)
            cv2.waitKey(1)

    

middle_frame = Frame(root, bg='blue', width=1000, height=150)
middle_frame.pack(side=TOP)

left_frame = Frame(root, bg='lightgreen', width=500, height=450)
left_frame.pack(side=LEFT)

right_frame = Frame(root, bg='#EAF6F6', width=500, height=450)
right_frame.pack(side=RIGHT)


image_open_btn = tk.Button(middle_frame,text = 'Open Image',fg = 'red',command = image_open_btn_clicked)
image_open_btn.config(width=22, height=2)
image_open_btn.place(x=200, y=75)

show_txt_btn = tk.Button(left_frame,text = 'Show text',fg = 'red', command = show_txt)
show_txt_btn.config(width=22, height=2)
show_txt_btn.place(x=200, y=50)

save_file_btn = tk.Button(middle_frame,text = 'Save Image',fg = 'red', command = save_image)
save_file_btn.config(width=22, height=2)
save_file_btn.place(x=700, y=75)

apply_OCR_btn = tk.Button(left_frame,text = 'Show OCR image',fg = 'red', command = show_ocr)
apply_OCR_btn.config(width=22, height=2)
apply_OCR_btn.place(x=200, y=125)

auto_crop_btn = tk.Button(left_frame,text = 'Auto Crop',fg = 'red', command = auto)
auto_crop_btn.config(width=22, height=2)
auto_crop_btn.place(x=200, y=200)

manual_crop_btn = tk.Button(left_frame,text = 'Manual Crop',fg = 'red', command = manual)
manual_crop_btn.config(width=22, height=2)
manual_crop_btn.place(x=200, y=275)

close_all_btn = tk.Button(left_frame,text = 'Close All',fg = 'red', command = close_all)
close_all_btn.config(width=22, height=2)
close_all_btn.place(x=200, y=350)


cv2.destroyAllWindows()
root.mainloop()