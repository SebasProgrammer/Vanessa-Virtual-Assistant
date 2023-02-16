from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from begin import WakeVanessa
from PyQt5 import QtGui
import sys
from global_variables import r, r1, m,  m2
from voice import speechRecognition
from database.retrieveDocuments import showAllDocuments
from insertDocumento import saveImageToDb
import re

class dLabel(QLabel):
    def __init__(self, widget):
        super(dLabel, self).__init__(widget)
        self.setAcceptDrops(True)
        self.filePath = ""
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
                    QLabel{
                        border: 4px dashed #aaa
                    } ''')
    def getFilePath(self):
        return self.filePath

    def dragEnterEvent(self, event):
        file_name = event.mimeData().text()
        if file_name.split('.')[-1] in ['png', 'jpg', 'jpeg']:
            self.filePath = file_name
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_path = event.mimeData().text()
        file_path = re.sub('file:///', '', file_path)
        self.setText(self.filePath)
        pixmap = QPixmap(file_path)
        self.setPixmap(pixmap)
        self.setScaledContents(True)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi('vanessa_model.ui', self)
        self.setWindowTitle('Vanessa')
        self.setWindowIcon(QtGui.QIcon('programmer-icon.jpg'))

        #retrieve data from database TAB1
        self.table = self.findChild(QTableWidget, "tableWidget")

        #Drag and drop image TAB2
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lineEdit.setFixedWidth(210)
        self.label = dLabel(self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.savePhoto)
        self.tabWidget = self.findChild(QWidget, "tab_2")
        tab2box = QVBoxLayout()
        tab2box.addWidget(self.lineEdit)
        tab2box.addWidget(self.label)
        tab2box.addWidget(self.button)
        self.tabWidget.setLayout(tab2box)

        #Show Initial GUI
        self.show()
        #Worker1
        self.worker = WorkerThread()
        self.worker.voice.connect(self.textUpdateSlot)
        self.worker.ans.connect(self.botAnswer)
        # #Worker2
        self.worker2 = WorkerThread2()
        self.worker2.table2.connect(self.showTable)
        self.worker2.voice2.connect(self.textActionSlot)
        self.worker2.ans2.connect(self.botAnswer)
        #Worker1 begins
        self.worker.start()

    #show table and getIMageLabel TAB1 FUNCTIONS
    def showTable(self):
        result, names = showAllDocuments('DOCUMENTO')
        self.table.setColumnCount(len(result[0]))
        self.table.setHorizontalHeaderLabels(names)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number==2:
                    item = self.getImageLabel(column_data)
                    self.table.setCellWidget(row_number, column_number, item)
                else:
                    self.table.setItem(row_number, column_number, QTableWidgetItem(item))
        self.table.verticalHeader().setDefaultSectionSize(80)

    def getImageLabel(self, image):
        imageLabel = QLabel(self.centralWidget())
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        imageLabel.setPixmap(pixmap)
        return imageLabel

    #Save Picture click button
    @pyqtSlot()
    def savePhoto(self):
        text = self.lineEdit.text()
        if not text:
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a name.")
            return
        saveImageToDb(self.label.getFilePath()[8:], text)
        self.label.filePath = ""
        self.lineEdit.clear()

    #CHAT APP
    def botAnswer(self, txt):
        self.sendandrec.append('\n' + 'Vanessa: ' + txt.capitalize() + '\n')

    def textActionSlot(self, txt):
        self.sendandrec.append('\n' + 'Tú: ' + txt.capitalize())

    def textUpdateSlot(self, txt):
        self.sendandrec.append('\n' + 'Tú: ' + txt.capitalize())
        self.worker.quit()
        self.worker2.start()

class WorkerThread(QThread):
    voice = pyqtSignal(str)
    ans = pyqtSignal(str)
    @pyqtSlot(str)
    def run(self):
        record, s = WakeVanessa(r,m)
        self.voice.emit(record)
        self.ans.emit(s)

class WorkerThread2(QThread):
    table2 = pyqtSignal()
    voice2 = pyqtSignal(str)
    ans2 = pyqtSignal(str)
    @pyqtSlot(str)
    def run(self):
        speechRecognition(r1, m2, self.voice2, self.ans2, self.table2)

app = QApplication(sys.argv)
UIWindow =UI()
app.exec()