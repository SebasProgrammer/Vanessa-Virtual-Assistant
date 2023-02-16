from speaking import speak
import webbrowser as wb
import pyautogui
from answer import AnswerSeconds
from global_variables import r2, m
from time import sleep
from keyboard import press_and_release

if __name__ == '__main__':
    r2.energy_threshold = 3000
    r2.dynamic_energy_threshold = False
    cnt = 0
    with m as source:
        r2.adjust_for_ambient_noise(source)
        while True:
            speak('¿Qué desea buscar?')
            r, source, text = AnswerSeconds(r2, source,2,6)
            if len(text) >= 3:
                pyautogui.hotkey('/')
                pyautogui.write(text)
                sleep(1)
                pyautogui.hotkey('enter')
                sleep(1)
                press_and_release('alt + space')
                sleep(1)
                press_and_release('x')
                sleep(1)
                pyautogui.moveTo(719, 320)
                speak('Tarea Completada')
                break
            elif cnt >0:
                speak('Lo lamento')
                speak('No se encontraron resultados')
                break
            speak('No entendí')
            cnt +=1