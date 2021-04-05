import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QScrollArea, QVBoxLayout, QWidget
import time


width = 800
height = 600

ImagePath = "Images/"

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Example")
        self.setGeometry(0,0, width, height)
        
        button = QPushButton("Botão caralho", self)
        button.move(600,0)
        button.clicked.connect(self.Action)

        self.scrollarea = QScrollArea(self)
        self.scrollarea.move(300,100)
        self.scrollarea.resize(300,300)

        self.vbox = QVBoxLayout()
        self.widget = QWidget()

        self.widget.setLayout(self.vbox)

    def Action(self):
        for i in range(12):
            self.label = QLabel(self)
            self.label.move(300,i *300)
            self.label.resize(300, 300)

            pixmap = QPixmap(f'{ImagePath}Image{i}.jpg')
            pixmapFixed = pixmap.scaled(300,300, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixmapFixed)

            self.vbox.addWidget(self.label)
        
        self.widget.setLayout(self.vbox)
        self.scrollarea.setWidget(self.widget)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()