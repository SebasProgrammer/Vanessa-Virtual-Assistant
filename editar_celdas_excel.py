from speaking import speak
import webbrowser as wb
import pyautogui
from answer import AnswerSeconds
from global_variables import r2, m
import re
from unicodedata import normalize
import openpyxl
import time

if __name__ == '__main__':
    r2.energy_threshold = 3000
    r2.dynamic_energy_threshold = False
    cnt = 0
    wb = openpyxl.load_workbook('./te.xlsx')
    with m as source:
        r2.adjust_for_ambient_noise(source)
        while True:
            speak('¿Qué desea editar?')
            r, source, text = AnswerSeconds(r2, source,2,6)
            if 'termina' in text:
                speak('Acción terminada')
                break
            text = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                normalize("NFD", text), 0, re.I
            )
            text = normalize('NFC', text)
            text = text.replace(' ', '')

            # Seleccionar una hoja de trabajo específica
            ws = wb['Ficha de Datos']
            s = "¿Cuál será el nuevo " + text +'?'
            speak(s)
            r, source, new_value = AnswerSeconds(r2, source, 2, 6)
            time.sleep(2)
            ws['B6'] = new_value
            wb.save('te.xlsx')
            speak('Celda editada con éxito')


