import cv2
import numpy as np
import pyautogui
from tesseract import image_to_string

src = 'sc3.jpg'

img = cv2.imread(src)

to_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




hor = np.hstack((img,to_gray))
cv2.imshow('Grey'hor[600:800])