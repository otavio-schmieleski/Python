import typing
from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
from interface_user import Ui_MainWindow
from Autentic_User import Autentic
import sys
from pathlib import Path
import json

ROOT_FOLDER = Path(__file__).parent / 'Users.json'
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'

try:
    with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
        banco = json.load(file)
    list(banco)
except FileNotFoundError:
    pass

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.stack_pags.setCurrentIndex(0)
        self.btn_inicial.clicked.connect(self.clicled_btn_iniciar)
        self.btn_option_transferir.clicked.connect(self.clicled_btn_transferir)
        self.btn_transf_ok.clicked.connect(self.clicled_btn_trans_ok)
        self.id_pag = 0
        self.btn_transferir.clicked.connect(self.clicled_btn_transf_ag)
        self.btn_option_consultar.clicked.connect(self.btn_clicled_option_consulta)
        self.btn_transf_voltar.clicked.connect(self.btn_tranf_voltar)

    def clicled_btn_iniciar(self):
        self.user_informado = self.line_nome.text()
        self.password_informado = self.line_senha.text()
        continua = True
        for user in banco:
            if self.user_informado == user['name'] and self.password_informado == user['password']:
                continua = False
        if continua == False:
            self.stack_pags.setCurrentIndex(1)
        else:
            self.func_aviso('Usuario ou senha incorreto!!!', 'OK',0)
    
    def clicled_btn_transferir(self):
        self.stack_pags.setCurrentIndex(2)
    
    def clicled_btn_trans_ok(self):
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        self.codigo_barras = self.line_cod_barra.text()
        for codigo in  banco_produtos:
            if self.codigo_barras == codigo['cod_barra']:
                self.codg = codigo['ag']
                self.stack_pags.setCurrentIndex(3)
            else:
                continue
    
    def btn_tranf_voltar(self):
        self.stack_pags.setCurrentIndex(1)
        
    def clicled_btn_transf_ag(self):
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        self.codigo_barras = self.line_cod_barra.text()
        for codigo in  banco_produtos:
            if self.codigo_barras == codigo['cod_barra']:
                try:
                    Ag = int(self.line_trans_ag.text())
                    if Ag >= 1 and Ag <= 31: 
                        self.ag = Ag
                        codigo['ag'] = self.ag
                        with open(ROOT_FOLDER_PRODUTOS, 'w', encoding='utf-8') as file:
                            json.dump(banco_produtos,file,ensure_ascii=False,indent=2)
                        self.func_aviso('Trasnferencia feita com Sucesso!!','OK',1)
                except TypeError and ValueError:
                    self.func_aviso('Informe uma agencia valida','OK',2)
                    pass
    
    def btn_clicled_option_consulta(self):
        self.stack_pags.setCurrentIndex(6)
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        for users in banco:
            if self.user_informado == users['name']:
                ag = users['ag']
                try:
                    with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                        banco_produtos = json.load(file)
                    list(banco_produtos)
                except FileNotFoundError:
                    pass
                self.tlabe_consulta.setRowCount(len(banco_produtos) + 2)
                self.tlabe_consulta.setColumnCount(len(banco_produtos))
                self.tlabe_consulta.setItem(0,0,QTableWidgetItem('PRODUTOS'))
                self.tlabe_consulta.setItem(0,1,QTableWidgetItem('AGENCIA'))
                self.tlabe_consulta.setItem(0,2,QTableWidgetItem('COD DE BARRAS'))

                for i,item in enumerate(banco_produtos):
                    if ag == item['ag']:
                        self.tlabe_consulta.setItem(i+1,0,QTableWidgetItem(item['name']))
                        self.tlabe_consulta.setItem(i+1,1,QTableWidgetItem(str(item['ag'])))
                        self.tlabe_consulta.setItem(i+1,2,QTableWidgetItem(item['cod_barra']))
                if len(item) == 0:
                    self.func_aviso('Nada de Imobilizados','OK',1)

    
    def func_aviso(self,mensagem,text_button,id_pags):
        self.stack_pags.setCurrentIndex(7)
        self.label_aviso.setText(f'{mensagem}')
        self.label_aviso.setStyleSheet('font-size: 14px; color: red; text-align: center;')
        self.btn_aviso.setText(f'{text_button}')
        self.btn_aviso.clicked.connect(self.clicled_btn_aviso)
        self.id_pag = id_pags

    def clicled_btn_aviso(self):
        self.line_nome.setText('')
        self.line_senha.setText('')
        self.stack_pags.setCurrentIndex(self.id_pag)

        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
