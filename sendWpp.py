#!/usr/bin/python
# -*- coding: cp1252 -*-
from time import sleep
import subprocess
import pyautogui
import psutil
import os
import cv2
from keyboard import press_and_release, press, release

def Running(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return False
    return False


photos = {'contacts': ['./whatsappContact.png', './whatsappContact2.png']}

def whatsappMsg():

    if (Running('WhatsApp') is True):
        os.system("taskkill /im WhatsApp.exe /F >nul 2>&1")

    try:
        subprocess.Popen(["cmd", "/C", "start whatsapp://"], shell=True)
        print('Se abrió WhatsApp Desktop')
    except:
        print('Debe instalar Whatsapp Desktop')
        return

    sleep(5)
    press('alt + space')
    sleep(1)
    press_and_release('x')
    sleep(1)
    release('alt + space')
    sleep(1)
    coordinates1 = None

    while coordinates1 is None and Running('Whatsapp.exe') == True:
        for photo in photos['contacts']:
            photo = cv2.imread(photo)
            coordinates1 = pyautogui.locateOnScreen(photo)
            if coordinates1 is None:
                pass
            else:
                x = coordinates1.left
                y = coordinates1.top
                pyautogui.click(x, y)
                sleep(1)
                # write(name)
                break

    if Running('Whatsapp.exe') is False:
        print('Se cerró WhatsApp Desktop')
        return
    else:
        if coordinates1 is None:
            print('No se encontró al contacto')
            return

if __name__ == '__main__':
    whatsappMsg()

