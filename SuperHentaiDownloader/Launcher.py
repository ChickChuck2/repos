from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (QAction, QApplication, QLabel, QLineEdit,
                             QMainWindow, QPushButton,
                             QScrollArea, QVBoxLayout, QWidget, qApp)
import SuperHentaiDownloader

class Launcher(QMainWindow):
    def __init__(self):
        super(Launcher, self).__init__()

        self.setWindowTitle("Super Hentai Launcher")
        self.setGeometry(0,0,SuperHentaiDownloader.width - 300,SuperHentaiDownloader.height - 300)

        LaunchApp = QPushButton("Iniciar", self)
        LaunchApp.clicked.connect(self.Launcher)
        LaunchApp.move(200,200)

        self.show()

    def Launcher(self):
        print("CU")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    
    #app.setStyleSheet(StyleDefault)
    
    sys.exit(app.exec_())