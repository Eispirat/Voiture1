# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formulaire1.ui'
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QPushButton, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox, QWidget
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_Dialog1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 597)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 150, 151, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 200, 151, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(self.compare_passwords)
        self.email_edit = self.lineEdit
        self.password_edit =self.lineEdit_2
        self.Cpassword_edit =self.lineEdit_3
        self.email_edit.setPlaceholderText("Entrez une adresse email Gmail")
        self.password_edit.setPlaceholderText("Entrez un mot de passe")
        self.Cpassword_edit.setPlaceholderText("Entrez une confirmation de mot de passe")
        self.cnx = mysql.connector.connect(user="root", password="", host="localhost", database="location_voiture")
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.pushButton_2.setText(_translate("Dialog", "Inscription"))
        self.label_3.setText(_translate("Dialog", "Confirmation:"))
        self.label.setText(_translate("Dialog", "Email:")) 
    def check_email(self):
        email = self.lineEdit.text()
        # Vérifier si l'adresse email se termine par "@gmail.com"
        if email == "":
            msg = QMessageBox()
            msg.setWindowTitle("Mot de Passe")
            msg.setText("Veuillez remplir le champ Email")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            if re.match(r"[^@]+@gmail\.com", email):
                self.lineEdit.setStyleSheet("")
                # Vérifier si l'adresse email existe dans la base de données
                cursor = self.cnx.cursor()
                cursor.execute("SELECT * FROM client WHERE email=%s", (email,))
                result = cursor.fetchone()
                if result is not None:
                    # L'email existe dans la base de données
                    print("L'email existe dans la base de données.")
                    msg = QMessageBox()
                    msg.setWindowTitle("Adresse email invalide")
                    msg.setText("L'email existe dans la base de données.")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec_()
                else:
                    return True
                cursor.close()
            else:
                self.lineEdit.setStyleSheet("QLineEdit { background-color: red; }")
                msg = QMessageBox()
                msg.setWindowTitle("Adresse email invalide")
                msg.setText("Veuillez entrer une adresse email valide'@gmail.com' ")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_() 
    def compare_passwords(self):
        password = self.lineEdit_2.text()
        cpassword = self.lineEdit_3.text()
        if password == cpassword:
            if password == "":
                msg = QMessageBox()
                msg.setWindowTitle("Mot de Passe")
                msg.setText("Veuillez remplir le mot de passe")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                if cpassword == "":
                    msg2 = QMessageBox()
                    msg2.setWindowTitle("Mot de Passe")
                    msg2.setText("Veuillez remplir la comfirmation du mot de passe")
                    msg2.setIcon(QMessageBox.Warning)
                    msg2.exec_()
            else:
                if self.check_email() == True:
                    self.insert_user_info()
                    msg = QMessageBox()
                    msg.setWindowTitle("Inscrption")
                    msg.setText("Inscription reuissite !")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec_() 
                 
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning mot de passe ")
            msg.setText("Veuillez entrer le meme mot de passe ")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_() 
    def insert_user_info(self):
    # Connect to the database
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="location_voiture"
        )

        # Create a cursor object
        cursor = db.cursor()

        # Define the INSERT statement
        sql = "INSERT INTO client (Email, Password) VALUES (%s, %s)"

        # Execute the INSERT statement with user data
        values = (email, password)
        cursor.execute(sql, values)

        # Commit the changes to the database
        db.commit()
        # Close the cursor and database connections
        cursor.close()
        db.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Dialog1()
    window.show()
    sys.exit(app.exec_())


