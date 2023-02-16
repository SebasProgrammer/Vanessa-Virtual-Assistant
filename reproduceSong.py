from speaking import speak
import webbrowser as wb
import pyautogui
from answer import AnswerSeconds
from global_variables import r2, m
from time import sleep

if __name__ == '__main__':
    r2.energy_threshold = 3000
    r2.dynamic_energy_threshold = False
    cnt = 0
    with m as source:
        r2.adjust_for_ambient_noise(source)
        while True:
            speak("Cuál es la canción?")
            r, source, sng = AnswerSeconds(r2, source,2,10)
            if len(sng) >= 3:
                pyautogui.write(sng)
                sleep(2)
                pyautogui.press('enter')
                sleep(1)
                pyautogui.press('tab')
                for i in range(2):
                    pyautogui.press('enter')
                    sleep(2)
                speak('Tarea Completada')
                break
            elif cnt > 0:
                speak('Lo lamento')
                speak('No se encontraron resultados')
                break
            speak('No entendí')
            cnt += 1


