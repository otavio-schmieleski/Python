# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QSize(412, 450))
        MainWindow.setMaximumSize(QSize(600, 450))
        icon = QIcon()
        icon.addFile(u"D:/dowloand/logo.jpeg", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setIconSize(QSize(100, 100))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(600, 450))
        self.stack_pags = QStackedWidget(self.centralwidget)
        self.stack_pags.setObjectName(u"stack_pags")
        self.stack_pags.setEnabled(True)
        self.stack_pags.setGeometry(QRect(0, 0, 591, 421))
        self.view_inicial = QWidget()
        self.view_inicial.setObjectName(u"view_inicial")
        self.view_inicial.setEnabled(True)
        self.titulo = QLabel(self.view_inicial)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(170, 20, 261, 20))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(12)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.btn_inicial = QPushButton(self.view_inicial)
        self.btn_inicial.setObjectName(u"btn_inicial")
        self.btn_inicial.setGeometry(QRect(260, 300, 75, 23))
        self.btn_inicial.setLayoutDirection(Qt.LeftToRight)
        self.btn_inicial.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(85, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.line_nome = QLineEdit(self.view_inicial)
        self.line_nome.setObjectName(u"line_nome")
        self.line_nome.setGeometry(QRect(200, 130, 201, 20))
        self.line_nome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_senha = QLineEdit(self.view_inicial)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setGeometry(QRect(200, 210, 201, 31))
        self.stack_pags.addWidget(self.view_inicial)
        self.view_principal = QWidget()
        self.view_principal.setObjectName(u"view_principal")
        self.view_principal.setEnabled(True)
        self.titulo_2 = QLabel(self.view_principal)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setGeometry(QRect(160, 0, 261, 20))
        self.titulo_2.setFont(font)
        self.titulo_2.setAlignment(Qt.AlignCenter)
        self.label_opcao = QLabel(self.view_principal)
        self.label_opcao.setObjectName(u"label_opcao")
        self.label_opcao.setGeometry(QRect(170, 60, 241, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_opcao.setFont(font1)
        self.label_opcao.setAlignment(Qt.AlignCenter)
        self.btn_option_transferir = QPushButton(self.view_principal)
        self.btn_option_transferir.setObjectName(u"btn_option_transferir")
        self.btn_option_transferir.setGeometry(QRect(180, 140, 201, 30))
        self.btn_option_transferir.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_option_consultar = QPushButton(self.view_principal)
        self.btn_option_consultar.setObjectName(u"btn_option_consultar")
        self.btn_option_consultar.setGeometry(QRect(180, 190, 201, 30))
        self.btn_option_consultar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_option_cadastrar = QPushButton(self.view_principal)
        self.btn_option_cadastrar.setObjectName(u"btn_option_cadastrar")
        self.btn_option_cadastrar.setGeometry(QRect(180, 240, 201, 30))
        self.btn_option_cadastrar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_option_user = QPushButton(self.view_principal)
        self.btn_option_user.setObjectName(u"btn_option_user")
        self.btn_option_user.setGeometry(QRect(180, 340, 201, 30))
        self.btn_option_user.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 13px\n"
"}")
        self.btn_cadastro_user = QPushButton(self.view_principal)
        self.btn_cadastro_user.setObjectName(u"btn_cadastro_user")
        self.btn_cadastro_user.setGeometry(QRect(180, 290, 201, 30))
        self.btn_cadastro_user.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.view_principal)
        self.view_transferencia = QWidget()
        self.view_transferencia.setObjectName(u"view_transferencia")
        self.view_transferencia.setEnabled(True)
        self.label_titulo = QLabel(self.view_transferencia)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(160, 30, 301, 20))
        self.label_titulo.setFont(font)
        self.line_cod_barra = QLineEdit(self.view_transferencia)
        self.line_cod_barra.setObjectName(u"line_cod_barra")
        self.line_cod_barra.setGeometry(QRect(120, 120, 311, 20))
        self.btn_scanner = QPushButton(self.view_transferencia)
        self.btn_scanner.setObjectName(u"btn_scanner")
        self.btn_scanner.setGeometry(QRect(450, 120, 61, 23))
        self.btn_scanner.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_transf_ok = QPushButton(self.view_transferencia)
        self.btn_transf_ok.setObjectName(u"btn_transf_ok")
        self.btn_transf_ok.setGeometry(QRect(350, 240, 75, 23))
        self.btn_transf_ok.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_transf_voltar = QPushButton(self.view_transferencia)
        self.btn_transf_voltar.setObjectName(u"btn_transf_voltar")
        self.btn_transf_voltar.setGeometry(QRect(170, 240, 75, 23))
        self.btn_transf_voltar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.view_transferencia)
        self.view_transferencia_ag = QWidget()
        self.view_transferencia_ag.setObjectName(u"view_transferencia_ag")
        self.view_transferencia_ag.setEnabled(True)
        self.label_titulo_ag = QLabel(self.view_transferencia_ag)
        self.label_titulo_ag.setObjectName(u"label_titulo_ag")
        self.label_titulo_ag.setGeometry(QRect(150, 0, 301, 20))
        self.label_titulo_ag.setFont(font)
        self.line_trans_ag = QLineEdit(self.view_transferencia_ag)
        self.line_trans_ag.setObjectName(u"line_trans_ag")
        self.line_trans_ag.setGeometry(QRect(159, 130, 271, 30))
        self.label_mostra_produto = QLabel(self.view_transferencia_ag)
        self.label_mostra_produto.setObjectName(u"label_mostra_produto")
        self.label_mostra_produto.setGeometry(QRect(90, 60, 210, 30))
        self.btn_transferir = QPushButton(self.view_transferencia_ag)
        self.btn_transferir.setObjectName(u"btn_transferir")
        self.btn_transferir.setGeometry(QRect(250, 220, 75, 30))
        self.btn_transferir.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(85, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.view_transferencia_ag)
        self.view_cadastro = QWidget()
        self.view_cadastro.setObjectName(u"view_cadastro")
        self.view_cadastro.setEnabled(True)
        self.label_cad_titulo = QLabel(self.view_cadastro)
        self.label_cad_titulo.setObjectName(u"label_cad_titulo")
        self.label_cad_titulo.setGeometry(QRect(170, 10, 251, 20))
        self.label_cad_titulo.setFont(font)
        self.line_cad_nome_produto = QLineEdit(self.view_cadastro)
        self.line_cad_nome_produto.setObjectName(u"line_cad_nome_produto")
        self.line_cad_nome_produto.setGeometry(QRect(190, 70, 201, 30))
        self.line_cad_agencia = QLineEdit(self.view_cadastro)
        self.line_cad_agencia.setObjectName(u"line_cad_agencia")
        self.line_cad_agencia.setGeometry(QRect(190, 130, 201, 30))
        self.line_cad_cod_barras = QLineEdit(self.view_cadastro)
        self.line_cad_cod_barras.setObjectName(u"line_cad_cod_barras")
        self.line_cad_cod_barras.setGeometry(QRect(190, 190, 201, 30))
        self.btn_cad_Scanner = QPushButton(self.view_cadastro)
        self.btn_cad_Scanner.setObjectName(u"btn_cad_Scanner")
        self.btn_cad_Scanner.setGeometry(QRect(410, 190, 75, 30))
        self.btn_cad_Scanner.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_cadastrar = QPushButton(self.view_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(250, 270, 75, 30))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_cad_voltar = QPushButton(self.view_cadastro)
        self.btn_cad_voltar.setObjectName(u"btn_cad_voltar")
        self.btn_cad_voltar.setGeometry(QRect(250, 320, 75, 30))
        self.btn_cad_voltar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.view_cadastro)
        self.view_user_cadastro = QWidget()
        self.view_user_cadastro.setObjectName(u"view_user_cadastro")
        self.view_user_cadastro.setEnabled(True)
        self.label_cad_user_titulo = QLabel(self.view_user_cadastro)
        self.label_cad_user_titulo.setObjectName(u"label_cad_user_titulo")
        self.label_cad_user_titulo.setGeometry(QRect(210, 30, 191, 20))
        self.label_cad_user_titulo.setFont(font)
        self.line_user_nome = QLineEdit(self.view_user_cadastro)
        self.line_user_nome.setObjectName(u"line_user_nome")
        self.line_user_nome.setGeometry(QRect(210, 100, 200, 30))
        self.line_user_agencia = QLineEdit(self.view_user_cadastro)
        self.line_user_agencia.setObjectName(u"line_user_agencia")
        self.line_user_agencia.setGeometry(QRect(210, 160, 200, 30))
        self.btn_user_cadastrar = QPushButton(self.view_user_cadastro)
        self.btn_user_cadastrar.setObjectName(u"btn_user_cadastrar")
        self.btn_user_cadastrar.setGeometry(QRect(270, 280, 75, 30))
        self.btn_user_cadastrar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(85, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.line_user_senha = QLineEdit(self.view_user_cadastro)
        self.line_user_senha.setObjectName(u"line_user_senha")
        self.line_user_senha.setGeometry(QRect(210, 220, 200, 30))
        self.btn_user_voltar = QPushButton(self.view_user_cadastro)
        self.btn_user_voltar.setObjectName(u"btn_user_voltar")
        self.btn_user_voltar.setGeometry(QRect(270, 330, 75, 30))
        self.btn_user_voltar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.view_user_cadastro)
        self.view_consulta = QWidget()
        self.view_consulta.setObjectName(u"view_consulta")
        self.view_consulta.setEnabled(True)
        self.label_titulo_consulta = QLabel(self.view_consulta)
        self.label_titulo_consulta.setObjectName(u"label_titulo_consulta")
        self.label_titulo_consulta.setGeometry(QRect(200, 0, 231, 20))
        self.label_titulo_consulta.setFont(font)
        self.btn_cons_voltar = QPushButton(self.view_consulta)
        self.btn_cons_voltar.setObjectName(u"btn_cons_voltar")
        self.btn_cons_voltar.setGeometry(QRect(150, 370, 75, 23))
        self.btn_cons_voltar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_cons_excluir = QPushButton(self.view_consulta)
        self.btn_cons_excluir.setObjectName(u"btn_cons_excluir")
        self.btn_cons_excluir.setGeometry(QRect(390, 370, 75, 23))
        self.btn_cons_excluir.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_cons_salvar = QPushButton(self.view_consulta)
        self.btn_cons_salvar.setObjectName(u"btn_cons_salvar")
        self.btn_cons_salvar.setGeometry(QRect(270, 370, 75, 23))
        self.btn_cons_salvar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 16px;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	font: 20px\n"
"}")
        self.tlabe_consulta = QTableWidget(self.view_consulta)
        self.tlabe_consulta.setObjectName(u"tlabe_consulta")
        self.tlabe_consulta.setGeometry(QRect(60, 70, 501, 291))
        self.lineEdit = QLineEdit(self.view_consulta)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(182, 40, 161, 20))
        self.label = QLabel(self.view_consulta)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 71, 20))
        self.pushButton = QPushButton(self.view_consulta)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 40, 75, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.pushButton_2 = QPushButton(self.view_consulta)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 40, 75, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.view_consulta)
        self.view_aviso = QWidget()
        self.view_aviso.setObjectName(u"view_aviso")
        self.btn_aviso = QPushButton(self.view_aviso)
        self.btn_aviso.setObjectName(u"btn_aviso")
        self.btn_aviso.setGeometry(QRect(250, 210, 75, 23))
        self.btn_aviso.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.label_aviso = QLabel(self.view_aviso)
        self.label_aviso.setObjectName(u"label_aviso")
        self.label_aviso.setGeometry(QRect(140, 69, 311, 121))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_aviso.setFont(font2)
        self.label_aviso.setAlignment(Qt.AlignCenter)
        self.stack_pags.addWidget(self.view_aviso)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 20, 341, 20))
        self.label_2.setFont(font1)
        self.line_altera_nome = QLineEdit(self.widget)
        self.line_altera_nome.setObjectName(u"line_altera_nome")
        self.line_altera_nome.setGeometry(QRect(200, 80, 201, 30))
        self.line_altera_ag = QLineEdit(self.widget)
        self.line_altera_ag.setObjectName(u"line_altera_ag")
        self.line_altera_ag.setGeometry(QRect(200, 140, 201, 30))
        self.line_altera_senha = QLineEdit(self.widget)
        self.line_altera_senha.setObjectName(u"line_altera_senha")
        self.line_altera_senha.setGeometry(QRect(200, 200, 200, 30))
        self.btn_salve_user = QPushButton(self.widget)
        self.btn_salve_user.setObjectName(u"btn_salve_user")
        self.btn_salve_user.setGeometry(QRect(260, 260, 75, 23))
        self.btn_salve_user.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(85, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.widget)
        self.view_admin = QWidget()
        self.view_admin.setObjectName(u"view_admin")
        self.view_admin.setEnabled(True)
        self.label_4 = QLabel(self.view_admin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 10, 311, 20))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_5 = QLabel(self.view_admin)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 50, 51, 21))
        self.line_admin_procurar = QLineEdit(self.view_admin)
        self.line_admin_procurar.setObjectName(u"line_admin_procurar")
        self.line_admin_procurar.setGeometry(QRect(170, 50, 201, 20))
        self.btn_admin_procurar = QPushButton(self.view_admin)
        self.btn_admin_procurar.setObjectName(u"btn_admin_procurar")
        self.btn_admin_procurar.setGeometry(QRect(400, 50, 75, 23))
        self.btn_admin_procurar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.list_admin_user = QTableWidget(self.view_admin)
        self.list_admin_user.setObjectName(u"list_admin_user")
        self.list_admin_user.setEnabled(True)
        self.list_admin_user.setGeometry(QRect(70, 80, 471, 261))
        self.btn_admin_voltar = QPushButton(self.view_admin)
        self.btn_admin_voltar.setObjectName(u"btn_admin_voltar")
        self.btn_admin_voltar.setGeometry(QRect(120, 360, 75, 23))
        self.btn_admin_voltar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_admin_salvar = QPushButton(self.view_admin)
        self.btn_admin_salvar.setObjectName(u"btn_admin_salvar")
        self.btn_admin_salvar.setGeometry(QRect(220, 360, 75, 23))
        self.btn_admin_salvar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_admin_alterar = QPushButton(self.view_admin)
        self.btn_admin_alterar.setObjectName(u"btn_admin_alterar")
        self.btn_admin_alterar.setGeometry(QRect(330, 360, 75, 23))
        self.btn_admin_alterar.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.btn_admin_del = QPushButton(self.view_admin)
        self.btn_admin_del.setObjectName(u"btn_admin_del")
        self.btn_admin_del.setGeometry(QRect(430, 360, 75, 23))
        self.btn_admin_del.setStyleSheet(u"QPushButton{\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"	font: 14px\n"
"}")
        self.stack_pags.addWidget(self.view_admin)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stack_pags.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Controle Imobilizados", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"CONTROLE DE IMOBILIZADOS", None))
        self.btn_inicial.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.line_nome.setText("")
        self.line_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe seu Nome de Usu\u00e1rio", None))
        self.line_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe sua Senha", None))
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"CONTROLE DE IMOBILIZADOS", None))
        self.label_opcao.setText(QCoreApplication.translate("MainWindow", u"Escolha uma Op\u00e7\u00e3o", None))
        self.btn_option_transferir.setText(QCoreApplication.translate("MainWindow", u"TRANSFERIR IMOBILIZADO", None))
        self.btn_option_consultar.setText(QCoreApplication.translate("MainWindow", u"CONSULTA IMOBILIZADOS", None))
        self.btn_option_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR IMOBILIZADOS", None))
        self.btn_option_user.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACOES DE USUSARIOS", None))
        self.btn_cadastro_user.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USUARIO", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"TRANSFERENCIA DE IMOBILIZADOS", None))
        self.line_cod_barra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o codigo de barras de 8 digitos", None))
        self.btn_scanner.setText(QCoreApplication.translate("MainWindow", u"Scanner", None))
        self.btn_transf_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.btn_transf_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_titulo_ag.setText(QCoreApplication.translate("MainWindow", u"TRANSFERENCIA DE IMOBILIZADOS", None))
        self.line_trans_ag.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe a agencia para transferir", None))
        self.label_mostra_produto.setText("")
        self.btn_transferir.setText(QCoreApplication.translate("MainWindow", u"TRANFERIR", None))
        self.label_cad_titulo.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR IMOBILIZADOS", None))
        self.line_cad_nome_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o nome do Produto", None))
        self.line_cad_agencia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe a Agencia", None))
        self.line_cad_cod_barras.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o codigo de barras 8 digitos", None))
        self.btn_cad_Scanner.setText(QCoreApplication.translate("MainWindow", u"Scanner", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_cad_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_cad_user_titulo.setText(QCoreApplication.translate("MainWindow", u"CADASTRO USUARIO", None))
        self.line_user_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o nome para usuario", None))
        self.line_user_agencia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe a Agencia", None))
        self.btn_user_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.line_user_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe uma senha de 4 digitos ou mais", None))
        self.btn_user_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_titulo_consulta.setText(QCoreApplication.translate("MainWindow", u"CONSULTA IMOBILIZADOS", None))
        self.btn_cons_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_cons_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.btn_cons_salvar.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o codigo de barras", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PROCURAR:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PROCURAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"SCANNER", None))
        self.btn_aviso.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_aviso.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ALTERANDO CADASTRO USUARIO", None))
        self.line_altera_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe um Nome", None))
        self.line_altera_ag.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe a Agencia", None))
        self.line_altera_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe uma senha de 4 digitos ou mais", None))
        self.btn_salve_user.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES ADMINISTRADOR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Procurar:", None))
        self.btn_admin_procurar.setText(QCoreApplication.translate("MainWindow", u"PROCURAR", None))
        self.btn_admin_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.btn_admin_salvar.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.btn_admin_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.btn_admin_del.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
    # retranslateUi

