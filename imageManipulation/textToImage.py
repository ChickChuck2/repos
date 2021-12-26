from PIL import Image, ImageFont, ImageDraw
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QRadioButton
import sys


DirectoryMeme = "base/"

class Janela(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle("SAM: Meme generator")
        self.resize(470,400)

        self.radiomole = QRadioButton("Eis que",self)
        self.radiomole.move(0,300)


        self.show()

        myimage = Image.open("base.png")
        text = "incrivel"
        image_editable = ImageDraw.Draw(myimage)
        title_font = ImageFont.truetype('arial.ttf', 100)
        image_editable.text((0,0), text, (255,200,200), font=title_font)
        myimage.save("result.png")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Janela()
    mainWin.show()
    sys.exit(app.exec_())