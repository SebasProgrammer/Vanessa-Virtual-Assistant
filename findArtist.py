from speaking import speak
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from answer import AnswerSeconds
from global_variables import r2, m
from global_variables import client_ID, pwd_ID
import webbrowser as wb
import pyautogui
from time import sleep

if __name__ == '__main__':
    r2.energy_threshold = 3000
    r2.dynamic_energy_threshold = False
    cnt = 0
    with m as source:
        r2.adjust_for_ambient_noise(source)
        while True:
            speak("Cuál es el nombre del artista?")
            r, source, artist = AnswerSeconds(r2, source,2,10)

            if len(artist)>3:
                # sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_ID, pwd_ID))
                # result = sp.search(artist)
                speak('Reproduciendo mejores canciones del artista')
                os.system("taskkill /im Spotify.exe /F >nul 2>&1")
                wb.open(f'spotify:search:')
                sleep(15)
                pyautogui.write(artist)
                sleep(2)
                pyautogui.press('enter')
                sleep(1)
                for i in range(2):
                    pyautogui.press('tab')
                    sleep(1)
                pyautogui.press('enter')
                sleep(1)
                pyautogui.keyDown('alt')
                pyautogui.keyDown('space')
                pyautogui.press('x')
                pyautogui.keyUp('space')
                pyautogui.keyUp('alt')
                sleep(1)
                speak('Tarea Completada')
                break
            elif cnt >0:
                speak('Lo lamento')
                speak('No se encontraron resultados')
                break

            speak('No entendí')
            cnt +=1



