import cv2
import numpy as np

def nothing(x):
    pass

# Load image
image = cv2.imread('sc3.jpg')

# Create a window
cv2.namedWindow('image')
cv2.namedWindow('Trackbar')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'Trackbar', 0, 179, nothing)
cv2.createTrackbar('SMin', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('VMin', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('HMax', 'Trackbar', 0, 179, nothing)
cv2.createTrackbar('SMax', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('VMax', 'Trackbar', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'Trackbar', 179)
cv2.setTrackbarPos('SMax', 'Trackbar', 255)
cv2.setTrackbarPos('VMax', 'Trackbar', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'Trackbar')
    sMin = cv2.getTrackbarPos('SMin', 'Trackbar')
    vMin = cv2.getTrackbarPos('VMin', 'Trackbar')
    hMax = cv2.getTrackbarPos('HMax', 'Trackbar')
    sMax = cv2.getTrackbarPos('SMax', 'Trackbar')
    vMax = cv2.getTrackbarPos('VMax', 'Trackbar')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display result image
    cv2.imshow('image', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()