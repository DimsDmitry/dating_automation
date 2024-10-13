import pyautogui
from time import sleep
from random import randrange
sleep(3)
path = 'like.png'
cross = 'cross.png'
later = 'not_now.png'


while True:
    try:
        button = pyautogui.locateOnScreen(path, confidence=0.7)
        pyautogui.click(button)
        sleep(randrange(10, 22)/10)
    except:
        try:
            button = pyautogui.locateOnScreen(cross, confidence=0.7)
            pyautogui.click(button)
            sleep(randrange(10, 22) / 10)
        except:
            try:
                button = pyautogui.locateOnScreen(later, confidence=0.7)
                pyautogui.click(button)
                sleep(randrange(10, 22) / 10)
            except:
                print('Что-то пошло не так')
                break
    sleep(0.01)