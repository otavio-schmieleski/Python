# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inter_login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)


class Ui_MainWindow(QMainWindow,object):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(516, 801)
       
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 401, 671))
        self.label.setStyleSheet(u"border-image: url(imagens/background.jpeg);\n"
"border-radius: 25px")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 50, 361, 601))
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0,125);\n"
"border-radius: 20px")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 70, 181, 81))
        font = QFont()
        font.setFamilies([u"Gabriola"])
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(155, 320, 231, 61))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom: 2px solid rgba(240,240,240,190);\n"
"	padding-left: 10px;\n"
"	color: rgb(255,255,255)\n"
"}\n"
"QLineEdit:hover{\n"
"	border-bottom: 4px solid rgba(255,255,255,190);\n"
"}")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(155, 410, 231, 61))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom: 2px solid rgba(240,240,240,190);\n"
"	padding-left: 10px;\n"
"	color: rgb(255,255,255)\n"
"}\n"
"QLineEdit:hover{\n"
"	border-bottom: 4px solid rgba(255,255,255,190);\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 340, 35, 35))
        self.label_4.setStyleSheet(u"border-image: url(imagens/login.png);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 430, 35, 35))
        self.label_5.setStyleSheet(u"border-image: url(imagens/redifini_senha.png);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 540, 191, 61))
        font2 = QFont()
        font2.setFamilies([u"Gabriola"])
        font2.setPointSize(18)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 10), stop:1 rgba(0, 0, 0, 214));\n"
"	border:none;\n"
"	border-radius:25px\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid rgba(255,255,255,180);\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 20), stop:1 rgba(0, 0, 0, 240));\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 1px solid rgb(255,255,255);\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 30), stop:1 rgba(0, 0, 0, 260));\n"
"	font:30px\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 516, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"htht", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication()
    window = Ui_MainWindow()
    window.show()
    app.exec()