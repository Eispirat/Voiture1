from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_MainWindow
from inscrip import Ui_Dialog as inscrip
import sys




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
inscript =QtWidgets.QDialog()
uiinscrip = inscriptDialog()
uiinscrip.setupUi(inscript)
MainWindow.show()
sys.exit(app.exec_())

