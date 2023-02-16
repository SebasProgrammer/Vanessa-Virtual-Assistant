from keyboard import press_and_release
from time import sleep
import pyautogui

def changeApp():

    press_and_release('Windows + Tab')
    sleep(1)
    press_and_release('left')
    press_and_release('enter')
    sleep(1)
    press_and_release('alt + space')
    sleep(1)
    press_and_release('x')
    sleep(1)
