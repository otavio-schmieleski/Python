# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QWidget,QMainWindow)

class Ui_Form(QMainWindow):
    def __init__(self,parent = None):
        self.setupUi(self)
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(620, 626)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 0, 321, 111))
        font = QFont()
        font.setFamilies([u"Playball"])
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(37, 161, 255)")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 261, 71))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(16)
        font1.setItalic(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:rgb(119, 224, 255)")
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 170, 101, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.radioButton.setFont(font2)
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(40, 210, 82, 17))
        self.radioButton_2.setFont(font2)
        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(40, 250, 82, 17))
        self.radioButton_3.setFont(font2)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 320, 221, 41))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:rgb(119, 224, 255)")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(40, 400, 70, 17))
        self.checkBox.setFont(font2)
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(40, 440, 70, 17))
        self.checkBox_2.setFont(font2)
        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(40, 360, 70, 17))
        self.checkBox_3.setFont(font2)
        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(40, 470, 70, 17))
        self.checkBox_4.setFont(font2)
        self.pushButton = QPushButton(Form, clicked= lambda: self.btn_clicked())
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 560, 111, 31))
        self.label_final = QLabel(Form)
        self.label_final.setObjectName(u"label_final")
        self.label_final.setGeometry(QRect(220, 540, 351, 61))

        self.radioButton.toggled.connect(self.radio_selected)
        self.radioButton_2.toggled.connect(self.radio_selected)
        self.radioButton_3.toggled.connect(self.radio_selected)
        self.checkBox.setChecked(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def radio_selected(self):
        self.radio=''
        if self.radioButton.isChecked():
            self.radio = self.radioButton.text()
        if self.radioButton_2.isChecked():
            self.radio = self.radioButton_2.text()
        if self.radioButton_3.isChecked():
            self.radio = self.radioButton_3.text()
    
    def btn_clicked(self):
        check1 = ''
        check2 = ''
        check3 = ''
        check4 = ''

        if self.checkBox.isChecked():
            check1 = self.checkBox.text()
        if self.checkBox_2.isChecked():
            check2 = self.checkBox_2.text()
        if self.checkBox_3.isChecked():
            check3 = self.checkBox_3.text()
        if self.checkBox_4.isChecked():
            check4 = self.checkBox_4.text()
        self.label_final.setText(f'Pizza sabor: {self.radio}, adicionais: {check1 + check2 + check3 + check4}')

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pizzaria Dev", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Escolha o sabor da Piazza", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Mussarela", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"calabresa", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"frango", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Escolha os adicionais", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"cheddar", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"catupry", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Azeitona", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"Borda", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SALVAR E ENVIAR", None))
        self.label_final.setText("")
    # retranslateUi

app = QApplication(sys.argv)
window = Ui_Form()
window.show()
app.exec()