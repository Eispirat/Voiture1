# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clienti.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import re
import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QPushButton, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox, QWidget, QTableWidgetItem
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    selected_row = -1

    def onItemClicked(self, it):
        self.selected_row = it.row()
        # print(self.tableWidget.item(it.row(), 0).text())
        self.marque.setText(self.tableWidget.item(it.row(), 0).text())
        self.modele.setText(self.tableWidget.item(it.row(), 1).text())
        self.type_de_carburant.setText(self.tableWidget.item(it.row(), 2).text())
        self.nombre_de_place.setText(self.tableWidget.item(it.row(), 3).text())
        self.transmission.setText(self.tableWidget.item(it.row(), 4).text())
        self.prix_de_location.setText(self.tableWidget.item(it.row(), 5).text())
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1109, 700)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(90, 240, 881, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 580, 211, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Marque"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Modele"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Type de carburant"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Nombre de places"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Transmission"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Prix de location/j"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Image"))
        self.pushButton.setText(_translate("Form", "Show All Cars"))
        resLen = len(listOfCars)
        index = 0
        self.tableWidget.setRowCount(resLen)
        for item in listOfCars:
            print(index)
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(item[1])))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(item[2])))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(item[4])))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(item[5])))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(item[6])))
            self.tableWidget.setItem(index, 5, QTableWidgetItem(str(item[7])))
            index += 1
        
        self.tableWidget.itemClicked.connect(self.onItemClicked)

cnx = mysql.connector.connect(user="root", password="", host="localhost", database="location_voiture")
cursor = cnx.cursor()
cursor.execute("SELECT * FROM voiture")
listOfCars = cursor.fetchall()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
