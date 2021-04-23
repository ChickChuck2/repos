from PyQt5 import QtWidgets, uic
import Application
MainWindow = QtWidgets.QApplication([])
launcher = uic.loadUi("untitled.ui")


def loadApplication():
    print("Load")
    
    Application.AppLaunch.exec()
    Application.interface.show()

    launcher.hide()

launcher.pushButton.clicked.connect(loadApplication)

launcher.show()
MainWindow.exec()