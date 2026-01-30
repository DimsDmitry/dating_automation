import pyautogui
from time import sleep
from random import randrange

sleep(3)
like = 'like2.png'
geo_accept = 'geo_accept.png'
quit = 'quit.png'
reload = 'reload.png'
likes = 0

while True:
    try:
        button_like = pyautogui.locateOnScreen(like, confidence=0.7)
        pyautogui.click(button_like)
        likes += 1
        pyautogui.moveRel(50, 0, duration=0.5)
        sleep(randrange(10, 22) / 1000)
        if likes % 100 == 0:
            print('Сделано лайков:', likes)
    except pyautogui.ImageNotFoundException:
        try:
            button_geo = pyautogui.locateOnScreen(geo_accept, confidence=0.7)
            pyautogui.click(button_geo)
        except pyautogui.ImageNotFoundException:
            try:
                button_reload = pyautogui.locateOnScreen(reload, confidence=0.7)
                pyautogui.click(button_reload)
                sleep(5)
            except:
                pyautogui.scroll(-randrange(400, 600))
    sleep(0.001) # 0.01