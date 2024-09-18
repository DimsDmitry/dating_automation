import pyautogui
from time import sleep
from random import randrange
sleep(3)
path = 'like.png'
while True:
    try:
        button = pyautogui.locateOnScreen(path, confidence=0.7)
        pyautogui.click(button)
        sleep(randrange(10, 22)/10)
    except:
        pyautogui.scroll(-randrange(400, 600))
    sleep(0.01)