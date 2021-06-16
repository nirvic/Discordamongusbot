import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import requests
from config import *

#Among us bot
orb = cv2.ORB_create(nfeatures=2000)

victory = cv2.imread('victory.jpg',0)
defeat = cv2.imread('defeat.jpg',0)
crewmate = cv2.imread('crewmate.jpg',0)
impostor = cv2.imread('impostor.jpg',0)

who_is = cv2.imread('who_is.jpg',0)
voting_results = cv2.imread('voting_results.jpg',0)

role_example = [defeat,crewmate,impostor]
vote_example = [who_is,voting_results]

#Role check
def role_check(search_crop,role):
    kp1, des1 = orb.detectAndCompute(search_crop, None)
    kp2, des2 = orb.detectAndCompute(role, None)

    bf = cv2.BFMatcher()
    matches_role = bf.knnMatch(des1,des2,k=2)

    good = []
    for m,n in matches_role:
        if m.distance < 0.25*n.distance:
            good.append([m])

    result = cv2.drawMatchesKnn(search_crop,kp1,role,kp2,good,None,flags=2)
    if len(good) > 10:
        return True
    else:
        return False

    result = cv2.imshow('match',result)


#While loop for detecting screen
def screengrab():
    while True:
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, 0)

        role_crop = screenshot[120:334,360:1550]
        vote_crop = screenshot[100:190,545:1280]

        #cv2.imshow('Role',role_crop)
        #cv2.imshow('Vote',vote_crop)
        if role_check(role_crop,crewmate) or role_check(role_crop,impostor) == True:
            print('Mute all players')
            requests.get(f"http://{address}:{port}/mute")
        elif role_check(vote_crop,who_is) == True:
            print('check dead')
            requests.get(f"http://{address}:{port}/unmute")
        elif role_check(vote_crop,voting_results) == True:
            print('Mute')
            requests.get(f"http://{address}:{port}/mute")
        elif role_check(role_crop,victory) or role_check(role_crop,defeat) == True:
            print('Revive')
            requests.get(f"http://{address}:{port}/revive")
            
        print('.')
        cv2.waitKey(1000)
