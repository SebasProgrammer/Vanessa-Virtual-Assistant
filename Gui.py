from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from begin import WakeVanessa
from PyQt5 import QtGui
import sys
from global_variables import r, r1, m,  m2
from voice import speechRecognition

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi('vanessa_model.ui', self)
        self.setWindowTitle('Vanessa')
        self.setWindowIcon(QtGui.QIcon('programmer-icon.jpg'))
        # self.pushButton.clicked.connect(self.onsendcl)
        self.show()

        #Worker1
        self.worker = WorkerThread()
        self.worker.voice.connect(self.textUpdateSlot)
        self.worker.ans.connect(self.botAnswer)
        # #Worker2
        self.worker2 = WorkerThread2()
        self.worker2.voice2.connect(self.textActionSlot)
        self.worker2.ans2.connect(self.botAnswer)
        #Worker1 begins
        self.worker.start()

    def botAnswer(self, txt):
        self.sendandrec.append('\n' + 'Vanessa: ' + txt.capitalize() + '\n')

    def textActionSlot(self, txt):
        self.sendandrec.append('\n' + 'Tú: ' + txt.capitalize())

    def textUpdateSlot(self, txt):
        self.sendandrec.append('\n' + 'Tú: ' + txt.capitalize())
        self.worker.quit()
        self.worker2.start()

    # def onsendcl(self):
    #     if len(self.sendtext.text()) > 5:
    #         self.sendandrec.append('\n' + 'Tú: ' + self.sendtext.text() + '\n')
    #         self.sendtext.setText("")
    #
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
    #         if len(self.sendtext.text())>5:
    #             self.sendandrec.append('\n' + 'Tú: ' + self.sendtext.text() + '\n')
    #             self.sendtext.setText("")

class WorkerThread(QThread):
    voice = pyqtSignal(str)
    ans = pyqtSignal(str)
    @pyqtSlot(str)
    def run(self):
        record, s = WakeVanessa(r,m)
        self.voice.emit(record)
        self.ans.emit(s)

class WorkerThread2(QThread):
    voice2 = pyqtSignal(str)
    ans2 = pyqtSignal(str)
    @pyqtSlot(str)
    def run(self):
        speechRecognition(r1, m2, self.voice2, self.ans2)


app = QApplication(sys.argv)
UIWindow =UI()
app.exec()