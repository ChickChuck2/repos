import json
import os
import random
import sys
import time
import traceback

import discord_rpc
import requests
from loguru import logger
from notifypy import notify
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (QAction, QApplication, QLabel, QLineEdit,
                             QMainWindow, QPushButton,
                             QScrollArea, QVBoxLayout, QWidget, qApp)

sources = "Sources/"

icon = f"{sources}icon.png"

default = 'style.css'

ImagePath = "Hentai-Image/"
GifPath = "Hentai-Gif/"
FavPath = "Favoritos/"

AppName = "Super Hentais - Downloader"

width = 800
height = 600

formatJPEG = ".jpeg"
formatPNG = ".png"
formatGIF = ".gif"

completenotificationAudio = f"{sources}CompleteNotificationAudio.wav"

Configs = {}
Configs['RichPresence'] = []
Configs['Notification'] = []
Configs['ImageViewer'] = []

try:
    os.mkdir(ImagePath)
    os.mkdir(GifPath)
    os.mkdir(FavPath)
except OSError:
    print ("Pasta %s Já existe" % ImagePath)
    print ("Pasta %s Já existe" % GifPath)
    print ("Pasta %s Já existe" % FavPath)
else:
    print ("Sucesso na criação da pasta %s " % ImagePath)
    print ("Sucesso na criação da pasta %s " % GifPath)
    print ("Sucesso na criação da pasta %s " % FavPath)

def readyCallback(current_user):
    print('Seu usuario: {}'.format(current_user))
def disconnectedCallback(codeno, codemsg):
    print('Desconectado do Discord {}: {}'.format(
        codeno, codemsg))
def errorCallback(errno, errmsg):
    print('Um erro com Presença do discord foi ocorrido {}: {}'.format(
        errno, errmsg))
callbacks = {
    'ready': readyCallback,
    'disconnected': disconnectedCallback,
    'error': errorCallback,}

start = time.time()

class WorkerSignals(QObject):

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

    def stop(self):
        self.running = False
        print('received stop signal from window.')
        with self._lock:
            self._do_before_done()

class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()

        self.setWindowTitle(AppName)
        self.setGeometry(0,0,width,height)
        self.setWindowIcon(QtGui.QIcon(icon))

        logo = QtGui.QPixmap(f"{sources}imageSize.webp")

        #TAB
        self.tabWidget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabWidget)

        self.Downloader = QtWidgets.QWidget()
        self.tabWidget.addTab(self.Downloader, "Downloader")

        self.galeria = QtWidgets.QWidget()
        self.tabWidget.addTab(self.galeria, "Galeria")
        ###
        ##
        #
        #
        ##
        #TAB1
        self.Logo = QLabel(self.Downloader)
        self.Logo.setPixmap(logo)
        self.Logo.move(270,40)
        self.Logo.resize(157,31)

        self.hentaiv = QLabel(self.Downloader)
        self.hentaiv.move(160, 80)
        self.hentaiv.resize(400,400)

        self.line1 = QLabel("Quantidade:", self.Downloader)
        self.line1.move(230,505)
        
        self.textbox = QLineEdit(self.Downloader)
        self.textbox.move(300,500)

        #labelINFO
        self.baixados = QLabel("Imagens Baixada: ", self.Downloader)
        self.baixados.move(50,510)
        self.baixados.resize(150,20)

        self.accept = QPushButton("Baixar", self.Downloader)
        self.accept.move(300,530)
        self.accept.clicked.connect(self.iniciar)
        ###
        ##
        #
        #
        ##
        #Galeria
        self.GaleriaScroll = QScrollArea(self.galeria)
        self.GaleriaScroll.move(0,0)
        self.GaleriaScroll.resize(800,555)

        self.GaleriaScroll.setStyleSheet("""
                                         background: black;
                                         border: 1px solid red;
                                         color: red;""")

        self.reloadGallery = QPushButton("Recarregar Galeria", self.galeria)
        self.reloadGallery.clicked.connect(self.LoadGallery)
        self.reloadGallery.setIcon(QtGui.QIcon(f"{sources}reload.png"))
        self.reloadGallery.move(570,0)

        # >>Style<<
        self.Downloader.setStyleSheet(open(default).read())
        self.accept.setStyleSheet(open(default).read())
        self.textbox.setStyleSheet(open(default).read())
        self.line1.setStyleSheet(open(default).read())
        self.baixados.setStyleSheet(open(default).read())

        self.show()
        self.LoadGallery()
        self.showUI()
        

        self.threadpool = QThreadPool()
        #print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    #!@ Funções @!
    def showUI(self):
        menubar = self.menuBar()

        sair = QAction('&Sair', self)
        sair.setShortcut('ctrl+Q')
        sair.setStatusTip('Sair do programa (ctrl+Q)')
        sair.triggered.connect(qApp.quit)


        fileMenu = menubar.addMenu('&Arquivo')
        fileMenu.addAction(sair)

        defini = menubar.addMenu("Definições")
        
        self.RichPresence = QAction('Desativar Status discord', self, checkable=True)
        self.RichPresence.setChecked(False)
        defini.addAction(self.RichPresence)

        defini.addSeparator()

        self.notification = QAction('Desativar notificações', self, checkable=True)
        self.notification.setChecked(False)
        defini.addAction(self.notification)

        defini.addSeparator()

        self.imagePreview = QAction('Desativar Visualização de imagem', self, checkable=True)
        self.imagePreview.setChecked(True)
        defini.addAction(self.imagePreview)

        self.saveConfigs = QAction("Salvar Configs", self)
        self.saveConfigs.triggered.connect(self.SalvarConfigs)
        defini.addAction(self.saveConfigs)

        menubar.setStyleSheet(open(default).read())

        #CONFIGURAÇÕES
        try:
            self.carregarConfigs()
        except Exception as e:
            print(logger.error(str(e)+ "\n" +
                "Aconteceu um erro, mas não se preocupe, não é grave"))

            print("-="*40)
            print("Arquivo de configuração não existe")
            print("")
            print("Criando Arquivo de configurações")

            with open('Configs.json', 'w') as outfile:
                json.dump(Configs, outfile, indent=4)

            print("Arquivo de Configurações criado")
            print("-="*40)

    def LoadGallery(self):
        imagensGaleria = os.listdir(ImagePath)
        ImageQuantidade = len(imagensGaleria)

        self.vbox = QVBoxLayout(self.galeria)
        self.widget = QWidget(self.galeria)
        self.widget.setLayout(self.vbox)

        quantiImage = QLabel(f"Imagens: {ImageQuantidade}", self.galeria)
        quantiImage.move(575,25)
        quantiImage.setStyleSheet("""color: red;""")
        print(ImageQuantidade)
        quantiImage.setText(f"Imagens: {ImageQuantidade}")

        for i in range(ImageQuantidade):
            
            ImageDeleteButton = QPushButton(f"Deletar {imagensGaleria[i]}",self.galeria)
            ImageName = ImageDeleteButton.text().replace("Deletar ", "")

            ImageFavorite = QPushButton(f"Favoritar",self.galeria)

            ImageGalleryShow = QLabel(self.galeria)

            ImageGallery = QtGui.QPixmap(f'{ImagePath}{imagensGaleria[i]}')
            ImageGalleryFixed = ImageGallery.scaled(550,550, QtCore.Qt.KeepAspectRatio)
            ImageGalleryShow.setPixmap(ImageGalleryFixed)

            ImageDeleteButton.clicked.connect(lambda ch, ImageName=ImageName: os.remove(f"{ImagePath}"+ImageName))
            ImageDeleteButton.clicked.connect(lambda ch, ImageGalleryShow=ImageGalleryShow: ImageGalleryShow.setHidden(True))
            ImageDeleteButton.clicked.connect(lambda ch, HiddeButtonDelete=ImageDeleteButton: HiddeButtonDelete.setHidden(True))
            ImageDeleteButton.clicked.connect(lambda ch, HiddeButtonFav=ImageFavorite: HiddeButtonFav.setHidden(True))

            
            ImageFavorite.clicked.connect(lambda ch, ImageName=ImageName: os.replace(f"{ImagePath}{ImageName}", f"{FavPath}{ImageName}"))
            ImageFavorite.clicked.connect(lambda ch, Favoritado=ImageFavorite: Favoritado.setText("Favoritado 👍"))


            ImageDeleteButton.setStyleSheet("""
                                                 background-color: white;
                                                 """)
            ImageFavorite.setStyleSheet("""
                                             background-color: white;                                     
                                             """)

            self.vbox.addWidget(ImageDeleteButton)
            self.vbox.addWidget(ImageFavorite)
            self.vbox.addWidget(ImageGalleryShow)
            
        
        self.widget.setLayout(self.vbox)
        self.GaleriaScroll.setWidget(self.widget)

    
    def carregarConfigs(self):
        print("-="*40)
        print("Carregando Configurações..")

        with open('Configs.json') as json_file:
            data = json.load(json_file)

            for p in data['RichPresence']:
                if p == "False":
                    self.RichPresence.setChecked(False)
                if p == "True":
                    self.RichPresence.setChecked(True)

            for p in data['Notification']:
                if p == "False":
                    self.notification.setChecked(False)
                if p == "True":
                    self.notification.setChecked(True)
            
            for p in data['ImageViewer']:
                if p == "False":
                    self.imagePreview.setChecked(False)
                if p == "True":
                    self.imagePreview.setChecked(True)
            
        print("Carregado")
        print("-="*40)
    
    def SalvarConfigs(self):

        Configs['Notification'].clear()
        Configs['RichPresence'].clear()
        Configs['ImageViewer'].clear()
        
        Configs['Notification'].append(
            f'{self.notification.isChecked()}',)

        Configs['RichPresence'].append(
            f'{self.RichPresence.isChecked()}',)

        Configs['ImageViewer'].append(
            f'{self.imagePreview.isChecked()}')
        
        with open('Configs.json', 'w') as outfile:
            json.dump(Configs, outfile, indent=4)

    #não deletar o self
    def get_content_type(self, url):
        return requests.head(url).headers['Content-Type']

    def pregresso(self, i):
        print("%d%% done" % i)
        
    def baixar(self, progress_callback):
        self.getTextString = self.textbox.text()
        self.getTextValue = int(self.getTextString)

        #Notificação de aviso
        if self.notification.isChecked() == False:
            notificationComplete = Notify(
                default_notification_application_name="HentaiDownloader",
                default_notification_title="Aviso",
                default_notification_message="Avisaremos Por aqui quando baixarmos tudo :D (QUANDO TUDO ACABAR IRÁ SAIR UM GEMIDINHO )",
                default_notification_icon=icon
                )

            notificationComplete.send()

        for i in range(self.getTextValue):
            #progress_callback.emit(i*100/getTextValue)

            IDran = random.randrange(1, 111767)
            link = "{}".format(IDran)

            self.baixados.setText("Imagens Baixadas: %d" % i)

            #Discord init RichPresence
            if self.RichPresence.isChecked() == False:
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
            print("ID: " + link)
            
            #Se a imagem for JPEG
            print(verifyJPEG)
            if verifyJPEG == "image/jpeg":
                print(linkJPEG)
                ImageJPEGname = "Super-Hentai-Image-{}{}".format(IDran, formatJPEG)
                file = open(f"{ImagePath}{ImageJPEGname}", "wb")
                file.write(URLdirJPEG.content)
                file.close()

                imgQuality = Image.open(f"{ImagePath}{ImageJPEGname}")
                imgQuality.save(f"{ImagePath}{ImageJPEGname}", quality=100)

                #Preview Image
                if self.imagePreview.isChecked() == False:

                    self.HentaiView = QtGui.QPixmap(f"{ImagePath}{ImageJPEGname}")
                    scaledpreiew = self.HentaiView.scaled(400,400, QtCore.Qt.KeepAspectRatio)
                    self.hentaiv.setPixmap(scaledpreiew)

            #Se a imagem for PNG
            print(verifyPNG)
            if verifyPNG == "image/png":
                print(linkPNG)
                ImagePNGname = "Super-Hentai-Image-{}{}".format(IDran, formatPNG)
                file = open(f"{ImagePath}{ImagePNGname}", "wb")
                file.write(URLdirPNG.content)
                file.close()

                #Preview Image
                if self.imagePreview.isChecked() == False:

                    self.HentaiView = QtGui.QPixmap(f"{ImagePath}{ImagePNGname}")
                    scaledpreiew = self.HentaiView.scaled(400,400, QtCore.Qt.KeepAspectRatio)
                    self.hentaiv.setPixmap(scaledpreiew)

            #Verificar se é gif
            print(verifyGIF)
            if verifyGIF == "image/gif":
                print(linkGIF)
                ImageGIFname = "Super-Hentai-Image-{}{}".format(IDran, formatGIF)
                file = open(f"{GifPath}{ImageGIFname}", "wb")
                file.write(URLdirGIF.content)
                file.close()
                
                #Preview Image
                if self.imagePreview.isChecked() == False:

                    self.HentaiView = QtGui.QPixmap(f"{GifPath}{ImageGIFname}")
                    scaledpreiew = self.HentaiView.scaled(400,400, QtCore.Qt.KeepAspectRatio)
                    self.hentaiv.setPixmap(scaledpreiew)
            
            self.setWindowTitle("{}: {}".format(AppName,IDran))
            print("=-"*40)
            
        #Notificação de downloa completo
        if self.notification.isChecked() == False:
            notificationComplete = Notify(
                default_notification_application_name="HentaiDownloader",
                default_notification_title="Aviso Download",
                default_notification_message="Hentais Baixados {}".format(i + 1),
                default_notification_icon=icon,
                default_notification_audio=completenotificationAudio
                )
            notificationComplete.send()

    def completo(self):
        print("Completo!!")

    def iniciar(self):
        worker = Worker(self.baixar)

        worker.signals.finished.connect(self.completo)

        worker.signals.progress.connect(self.pregresso)

        self.threadpool.start(worker)

# cor da janela em (CSS)
StyleDefault = """
    Janela {
        background-color: black;
    }
    QLineEdit {
        background: rgba(255, 0, 0, 1.271);
        color: red;
        border: 1px solid red;
    }
    QTabWidget::pane {
        border: 1px solid darkgray;
        top:-1px;
        background: black;
    } 
    QTabBar::tab {
        background: gray; 
        border: 1px solid gray;
        padding: 5px;
    } 
    QTabBar::tab:selected { 
        background: white; 
        margin-bottom: -1px; 
    }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    
    app.setStyleSheet(StyleDefault)

    discord_rpc.shutdown()
    sys.exit(app.exec_())