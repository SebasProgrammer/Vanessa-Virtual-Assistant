import speech_recognition as sr
from PyQt5.QtWidgets import QWidget, QApplication
import sys
#Para wpp.py
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
m2 = sr.Microphone(device_index=0)
#Para voice.py
r1 = sr.Recognizer()
# m1 = sr.Microphone(device_index=1)
#Para subprocesos como youtube.py, etc
r2 = sr.Recognizer()
# m2 = sr.Microphone(device_index=1)

#Para spotify
client_ID = '91a4b17721e34dd3bfde327815aa5386'
pwd_ID = 'af6f59bceeb645ecbc93245c2fa51033'

#Para model UI
app = QApplication(sys.argv)
widget = QWidget()