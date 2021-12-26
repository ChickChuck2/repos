from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
import sys

width = 800
height = 600

class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()
        uic.loadUi("Main.ui",self)

        self.show()
    
    def handleButton(self):
        print("cu")





app = QtWidgets.QApplication(sys.argv)
janela = Janela()
app.exec_()