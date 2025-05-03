from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
import sys
from ai import Ui_MainWindow


class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()
        
StartExe = MainThread()

class StartExecution(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.label = QMovie("C:\\Users\\HP\\My AI assistant\\Database\\Gui Material\\1.gif")

        self.ui.gif.setMovie(self.ui.label)

        self.ui.label.start()

        StartExe.start()

App = QApplication(sys.argv)
speedtest = StartExecution()
speedtest.show()
exit(App.exec_())
        