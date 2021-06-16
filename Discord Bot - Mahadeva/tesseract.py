import cv2
import pytesseract
import numpy as np
from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

src = 'sc3.jpg'
img = cv2.imread(src)
to_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(to_gray, (7,7), 0)

simg = cv2.resize(img,(720,480))
sto_gray = cv2.resize(to_gray,(720,480))

pos1 = img_blur[218:274,396:633]

kernel = np.ones((15,15), np.uint8)

def empty():
    pass

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', (640,240))
cv2.createTrackbar('T1','Trackbar', 0, 1000,empty)
cv2.createTrackbar('T2','Trackbar', 0, 1000,empty)

while True:
    t1 = cv2.getTrackbarPos('T1','Trackbar')
    t2 = cv2.getTrackbarPos('T2','Trackbar')

    to_canny = cv2.Canny(pos1,t1,t2)
    to_ero = cv2.dilate(to_canny, kernel, iterations=22)
    cv2.imshow('pos1', pos1)
    cv2.imshow('Image',to_canny)

    print(pytesseract.image_to_string(pos1))
    print(pytesseract.image_to_string(to_canny))

    cv2.waitKey(1)

#print(pytesseract.image_to_string(pos1))
#print(pytesseract.image_to_string(to_canny))


#cv2.imshow('Image1',simg)
#cv2.imshow('Image',sto_gray)
cv2.imshow('Image',to_canny)
#cv2.imshow('Image',img_blur)





cv2.waitKey(0)