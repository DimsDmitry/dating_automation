import pyautogui
from time import sleep
from random import randrange

sleep(3)
like = 'like.png'
geo_accept = 'geo_accept.png'
quit = 'quit.png'

while True:
    try:
        button_like = pyautogui.locateOnScreen(like, confidence=0.7)
        pyautogui.click(button_like)
        sleep(randrange(10, 22) / 10)
    except pyautogui.ImageNotFoundException:
        try:
            button_geo = pyautogui.locateOnScreen(geo_accept, confidence=0.7)
            pyautogui.click(button_geo)
        except pyautogui.ImageNotFoundException:
            pyautogui.scroll(-randrange(400, 600))

    sleep(0.01)
