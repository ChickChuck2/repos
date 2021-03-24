import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit, QPushButton, QApplication
from PyQt5 import QtGui
import random
import time
import requests
import discord_rpc
import os
from notifypy import Notify

default = 'style.css'
imageDir = "Hentai-Image/"
gifDir = "Hentai-Gif/"

icon = "Sources/icon.png"

width = 800
height = 600

formatJPEG = ".jpeg"
formatPNG = ".png"
formatGIF = ".gif"

completenotificationAudio = "Sources\CompleteNotificationAudio.wav"

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

start = time.time()
i = 0

class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()

        self.setWindowTitle("Super Hentai Downloader")
        self.setWindowIcon(QtGui.QIcon(icon))

        logo = QtGui.QPixmap("Sources/imageSize.webp")

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
        self.accept.setStyleSheet(open(default).read())
        self.textbox.setStyleSheet(open(default).read())
        
        self.show()
    
    #!@ Funções @!
    def get_content_type(self, url):
        return requests.head(url).headers['Content-Type']
        
    def baixar(self):
        self.getTextString = self.textbox.toPlainText()
        getTextValue = int(self.getTextString)

        notificationComplete = Notify(
            default_notification_application_name="HentaiDownloader",
            default_notification_title="Aviso",
            default_notification_message="Avisaremos Por aqui quando baixarmos tudo :D (QUANDO TUDO ACABAR IRÁ SAIR UM GEMIDINHO )",
            default_notification_icon=icon
            )
        notificationComplete.send()

        for i in range(getTextValue):
            IDran = random.randrange(1, 111767)
            link = "ID: {}".format(IDran)

            #Discord init RichPresence
            discord_rpc.initialize('816485448666578984', callbacks=callbacks, log=False)
            discord_rpc.update_presence(
                **{
                    'details': 'Baixando Hentai ID: {}'.format(IDran),
                    'state': 'Baixei {} Hentais 😎🤙'.format(i),
                    'start_timestamp': start,
                    ''
                    'large_image_key': 'android-chrome-512x512'
                }
            )
            discord_rpc.update_connection()
            time.sleep(1)
            discord_rpc.run_callbacks()
            
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
            
        #Notificação de downloa completo
        notificationComplete = Notify(
            default_notification_application_name="HentaiDownloader",
            default_notification_title="Aviso Download",
            default_notification_message="Hentais Baixados {}".format(i + 1),
            default_notification_icon=icon,
            default_notification_audio=completenotificationAudio
            )
        notificationComplete.send()

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

    discord_rpc.shutdown()

    sys.exit(app.exec_())