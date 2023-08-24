# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled_01.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from typing import Optional
import PySide6
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(QMainWindow):
    def __init__(self, parent =None) :
        super().__init__(parent)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(534, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.btn_add = QPushButton(self.centralwidget,clicked =self.add_item)
        self.btn_add.setObjectName(u"btn_add")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_add.setFont(font)

        self.verticalLayout.addWidget(self.btn_add)

        self.btn_del = QPushButton(self.centralwidget, clicked= self.del_item)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setFont(font)

        self.verticalLayout.addWidget(self.btn_del)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.btn_clear = QPushButton(self.centralwidget, clicked= self.clear_item)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFont(font)

        self.verticalLayout.addWidget(self.btn_clear)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 534, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def add_item(self):
        item = self.lineEdit.text()
        self.listWidget.addItem(item) # adiciona o item na lista
        self.lineEdit.setText('')
    
    def del_item(self):
        item = self.listWidget.currentRow() # retona o numero da linha selecionada
        self.listWidget.takeItem(item) # esclui a linha passada

    def clear_item(self):
        self.listWidget.clear() # limpa a lista inteira

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"adicionar", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"excluir", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"limpar", None))
    # retranslateUi

app = QApplication(sys.argv)
window = Ui_MainWindow()
window.show()
app.exec()