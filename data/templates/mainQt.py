from data.appdata.functions import *
from data.appdata.classes import *

import sys
from PyQt5 import uic
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/design/"yourUI".ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())