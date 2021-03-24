import sys
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import random
import time
import requests
import discord_rpc
import os

default = 'style.css'
imageDir = "Hentai-Image/"
gifDir = "Hentai-Gif/"

icon = "icon.png"
width = 800
height = 600

formatJPEG = ".jpeg"
formatPNG = ".png"
formatGIF = ".gif"

try:
    os.mkdir(imageDir)
    os.mkdir(gifDir)
except OSError:
    print ("falha na criação da pasta %s " % imageDir)
    print ("falha na criação da pasta %s " % gifDir)
else:
    print ("Sucesso na criação da pasta %s " % imageDir)
    print ("Sucesso na criação da pasta %s " % gifDir)

def readyCallback(current_user):
    print('Our user: {}'.format(current_user))
def disconnectedCallback(codeno, codemsg):
    print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
        codeno, codemsg
))
def errorCallback(errno, errmsg):
    print('An error occurred! Error {}: {}'.format(
        errno, errmsg
))
callbacks = {
    'ready': readyCallback,
    'disconnected': disconnectedCallback,
    'error': errorCallback,
}
discord_rpc.initialize('816485448666578984', callbacks=callbacks, log=False)
#Discord presence
start = time.time()
i = 0
class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()

        self.setWindowTitle("Super Hentai Downloader")
        self.setWindowIcon(QtGui.QIcon(icon))

        logo = QtGui.QPixmap("imageSize.webp")

        self.label = QLabel(self)
        self.label.setPixmap(logo)
        self.label.move(270,0)
        self.label.resize(157,31)

        self.setGeometry(0,0,width,height)

        self.textbox = QTextEdit(self)
        self.textbox.move(300,500)
        self.textbox.resize(100,25)

        self.accept = QPushButton("Baixar", self)
        self.accept.move(300,530)
        self.accept.clicked.connect(self.baixar)

        
        # >>Style<<
        
        self.show()
    
    #!@ Funções @!
    def get_content_type(self, url):
        return requests.head(url).headers['Content-Type']
        
    def baixar(self):
        self.getTextString = self.textbox.toPlainText()
        getTextValue = int(self.getTextString)
        for i in range(getTextValue):
            IDran = random.randrange(1, 111767)
            link = "ID: {}".format(IDran)
            
            #JPEG/JPG
            linkJPEG = "https://figure.superhentais.com/img/figure/{}{}.download".format(IDran, formatJPEG)
            URLdirJPEG = requests.get(linkJPEG)
            verifyJPEG = self.get_content_type(linkJPEG)
            #PNG
            linkPNG = "https://figure.superhentais.com/img/figure/{}{}.download".format(IDran, formatPNG)
            URLdirPNG = requests.get(linkPNG)
            verifyPNG = self.get_content_type(linkPNG)
            #GIF
            linkGIF = "https://figure.superhentais.com/img/figure/{}{}.download".format(IDran, formatGIF)
            URLdirGIF = requests.get(linkGIF)
            verifyGIF = self.get_content_type(linkGIF)
            ###########
            ###########
            print(link)

            print(verifyJPEG)
            #Se a imagem for JPEG
            if verifyJPEG == "image/jpeg":
                ImageJPEGname = "Super-Hentai-Image-{}{}".format(IDran, formatJPEG)
                file = open(f"{imageDir}{ImageJPEGname}", "wb")
                file.write(URLdirJPEG.content)
                file.close()
            #Verificar se é PNG
            else:
                verifyPNG
                print(verifyPNG)
                #Se a imagem for PNG
                if verifyPNG == "image/png":
                    ImagePNGname = "Super-Hentai-Image-{}{}".format(IDran, formatPNG)
                    file = open(f"{imageDir}{ImagePNGname}", "wb")
                    file.write(URLdirPNG.content)
                    file.close()
                #Verificar se é gif
                else:
                    verifyGIF
                    print(verifyGIF)
                    #Se for GIF
                    if verifyGIF == "image/gif":
                        ImageGIFname = "Super-Hentai-Image-{}{}".format(IDran, formatGIF)
                        file = open(f"{gifDir}{ImageGIFname}", "wb")
                        file.write(URLdirGIF.content)
                        file.close()
                    else:
                        print("Não foi possivel verificar tipo do arquivo. Arquivo e outro formato desconhecido, ou a ID {} Não existe.".format(IDran))
            print("=-"*40)

# cor da janela em (CSS)
df = """
    Janela {
        background-color: black;
    }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet(df)
    janela = Janela()
    janela.show()

    sys.exit(app.exec_())