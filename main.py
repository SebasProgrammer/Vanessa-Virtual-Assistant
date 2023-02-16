import sys
import threading
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from global_variables import app, widget
from PyQt5.QtWidgets import QWidget, QApplication
from wpp import WakeVanessa

def prunt():
    while True:
        print("chau")
        time.sleep(1)


class myclass(QWidget):
    def __init__(self):
        super(myclass, self).__init__()
        loadUi('vanessa_model.ui', self)
        self.setWindowTitle('arvendra')
        self.pushButton.clicked.connect(self.onsendcl)
        # self.sendandrec.keyPressEvent(self, QKeyEvent)

    def onsendcl(self):
        self.sendandrec.append('\n' + 'you: ' + self.sendtext.text() + '\n')
        self.sendtext.setText("")


app = QApplication(sys.argv)
widget = myclass()
widget.show()
sys.exit(app.exec())
soc.close()