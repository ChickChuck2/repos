from image_to_ascii import ImageToAscii as Ascii
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon
import sys

class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()
        self.setGeometry(0,0,300,300)

        self.setWindowTitle("My Ascii generator")
        
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela()
    sys.exit(app.exec_())
Ascii(imagePath="img.jpg",outputFile="outfile.txt",witdh=40)