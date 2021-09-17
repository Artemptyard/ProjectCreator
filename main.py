from data.appdata.functions import QtCreater, cmdCreater, WebCreater
#from data.appdata.clases import *

import sys
from PyQt5 import uic
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import os
import shutil


class Creater(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/design/creater.ui', self)
        self.createBTN.clicked.connect(self.createProject)
        self.pType.activated.connect(self.changeType)

    def createProject(self):
        fPath = QFileDialog.getSaveFileName(
            self, 'Выбрать',
            self.pName.text(), 'Все файлы (*)')[0]
        os.mkdir(fPath)
        if self.pType.currentIndex() == 0:
            Data = self.Qt_1.isChecked()
            Design = self.Qt_2.isChecked()
            Img = self.Qt_3.isChecked()
            Files = self.Qt_4.isChecked()
            AppD = self.Qt_5.isChecked()
            Db = self.Qt_6.isChecked()
            QtCreater(fPath, Data, Design, Img, Files, AppD, Db)
        elif self.pType.currentIndex() == 1:
            Data = self.cmd_1.isChecked()
            Img = self.cmd_2.isChecked()
            Files = self.cmd_3.isChecked()
            AppD = self.cmd_4.isChecked()
            Db = self.cmd_5.isChecked()
            cmdCreater(fPath, Data, Img, Files, AppD, Db)
        else:
            Temp = self.web_1.isChecked()
            Static = self.web_2.isChecked()
            Img = self.web_3.isChecked()
            Css = self.web_4.isChecked()
            Files = self.web_5.isChecked()
            AppD = self.web_6.isChecked()
            Db = self.web_7.isChecked()
            WebCreater(fPath, Temp, Static, Img, Css, Files, AppD, Db)

    def changeType(self):
        self.pTypes.setCurrentIndex(self.pType.currentIndex())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Creater()
    ex.show()
    sys.exit(app.exec_())