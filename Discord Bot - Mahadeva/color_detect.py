import cv2 
import numpy as np
import sys
import tesseract
import pyautogui
np.set_printoptions(threshold=sys.maxsize)

image = cv2.imread('sc3.jpg')


hMin = 0 
sMin = 255
vMin = 0

hMax = 2
sMax = 255
vMax = 255

low_dead = np.array([hMin,sMin,vMin])
high_dead = np.array([hMax,sMax,vMax])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, low_dead, high_dead)

result = cv2.bitwise_and(image, image, mask=mask)
image = cv2.circle(image, (999,810), 1, (0,255,0), 2)



#dead_mask = np.transpose(np.nonzero(mask))
#cv2.imshow('Result', image)
#print(dead_mask)

if (999,810) in dead_mask:
    print('Dead')
else:
    print('alive')



#Check positions Y, X

#Ded x color values hMin = 6, sMin = 123, vMin = 118, hMax = 16, sMax = 255, vMax = 255

#Lime = (hMin = 40 , sMin = 89, vMin = 118), (hMax = 84 , sMax = 149, vMax = 156)
#Yellow = (hMin = 29 , sMin = 51, vMin = 112), (hMax = 53 , sMax = 122, vMax = 179)
#Red = (hMin = 161 , sMin = 80, vMin = 85), (hMax = 179 , sMax = 255, vMax = 153)
#Blue = (hMin = 110 , sMin = 52, vMin = 87), (hMax = 117 , sMax = 172, vMax = 158)
#Teal = (hMin = 83 , sMin = 119, vMin = 126), (hMax = 102 , sMax = 165, vMax = 167)


cv2.waitKey()
cv2.destroyAllWindows()