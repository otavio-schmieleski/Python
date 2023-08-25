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
        self.btn_cons_excluir.clicked.connect(self.btn_cons_del)
        self.btn_cons_salvar.clicked.connect(self.btn_cons_salvar_banco)
        self.btn_cons_voltar.clicked.connect(self.btn_cons_voltar_inicio)
        self.btn_option_cadastrar.clicked.connect(self.btn_cadastro_inicio)
        self.btn_cadastrar.clicked.connect(self.btn_cadastrar_produtos)
        self.btn_cadastro_user.clicked.connect(self.btn_cadastrar_user)
        self.btn_user_cadastrar.clicked.connect(self.btn_cadastrar_usuario)

    def clicled_btn_iniciar(self):
        self.user_informado = self.line_nome.text()
        self.password_informado = self.line_senha.text()
        continua = True
        for user in banco:
            if self.user_informado == user['self.name'] and self.password_informado == user['password']:
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
            if self.user_informado == users['self.name']:
                ag = users['ag']
                try:
                    with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                        banco_produtos = json.load(file)
                    list(banco_produtos)
                except FileNotFoundError:
                    pass
                self.tlabe_consulta.setRowCount(len(banco_produtos) + 1)
                self.tlabe_consulta.setColumnCount(3)
                self.tlabe_consulta.setItem(0,0,QTableWidgetItem('PRODUTOS'))
                self.tlabe_consulta.setItem(0,1,QTableWidgetItem('AGENCIA'))
                self.tlabe_consulta.setItem(0,2,QTableWidgetItem('COD DE BARRAS'))
                try:
                    for i,item in enumerate(banco_produtos):
                        if ag == item['ag']:
                            self.tlabe_consulta.setItem(i+1,0,QTableWidgetItem(item['self.name']))
                            self.tlabe_consulta.setItem(i+1,1,QTableWidgetItem(str(item['ag'])))
                            self.tlabe_consulta.setItem(i+1,2,QTableWidgetItem(item['cod_barra']))
                    if len(item) == 0:
                        self.func_aviso('Nada de Imobilizados','OK',1)
                except:
                    self.func_aviso('Nada de Imobilizados','OK',1)

    def btn_cons_del(self):
        produto_selecionado = self.tlabe_consulta.currentRow()
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        del banco_produtos[produto_selecionado - 1]
        with open(ROOT_FOLDER_PRODUTOS, 'w', encoding='utf-8') as file:
            json.dump(banco_produtos,file,ensure_ascii=False,indent=2)
        self.btn_clicled_option_consulta()
        
    def btn_cons_salvar_banco(self):
        self.func_aviso('Salvo com Sucesso!','OK',1)
    
    def btn_cons_voltar_inicio(self):
        self.stack_pags.setCurrentIndex(1)

    def btn_cadastro_inicio(self):
        self.stack_pags.setCurrentIndex(4)

    def btn_cadastrar_produtos(self):
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        global P_Name
        # nome do produto para cadastrar
        P_Name = self.line_cad_nome_produto.text()
        if P_Name == "" or P_Name == " " or P_Name =="  " or P_Name == "   ":
            self.func_aviso('Informe um nome valido','OK',4)
            self.line_cad_nome_produto.clear()
        else:
            self.self.name = P_Name
        global P_Ag
        try:
            P_Ag = int(self.line_cad_agencia.text())
            if P_Ag >= 1 and P_Ag <= 31: 
                self.ag = P_Ag
        except TypeError and ValueError:
            self.func_aviso('Informe uma agencia valida','OK',4)
            self.line_cad_agencia.clear()
        global codigo_barras
        codigo_barras = self.line_cad_cod_barras.text()
        if codigo_barras.isdigit() and len(codigo_barras) == 8:
            continua = True
            for codigo in banco_produtos:
                if codigo_barras in codigo['cod_barra']:
                    continua = False
            if continua == False:
                self.func_aviso('Informe um codigo de barras valido','OK',4)
                self.line_cad_cod_barras.clear()
            else:
                self.cod_barra = codigo_barras
                pass

        # armazenando no banco de dados
        def Banco_de_dados_produtos(valor):
            banco.append(vars(valor))
            with open(ROOT_FOLDER_PRODUTOS,'w',encoding='utf-8') as file:
                json.dump(banco_produtos,file,ensure_ascii=False,indent=2)

        class banco_valores:
            def __init__(self,valor1,valor2,valor3):
                self.self.name = valor1
                self.ag = valor2
                self.cod_barra = valor3

        if P_Name != None and P_Ag != None and codigo_barras != None:
            p2 = banco_valores(P_Name,P_Ag,codigo_barras)
            Banco_de_dados_produtos(p2)
            self.func_aviso("Produto cadastrado com sucesso!!",'OK',1)

    def btn_cadastrar_user(self):
        self.stack_pags.setCurrentIndex(5)

    def btn_cadastrar_usuario(self):
        self.Name = None
        self.Ag = None
        self.Password = None
        banco = []
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        self.name = self.line_user_nome.text()
        continua = True
        for usuario in banco:
            if self.name == usuario['name'] or self.name == "" or self.name == " " or self.name =="  " or self.name == "   ":
                continua = False
        if continua == False:
            self.func_aviso('Usuario ja cadastrado','OK',5)
            self.line_user_nome.clear()
        else:
            self.Name = self.name
        try:
            self.ag = int(self.line_user_agencia.text())
            if self.ag >= 1 and self.ag <= 31:
                self.Ag = self.ag
            else:
                self.func_aviso('Agencia invalida','OK',5)
                self.line_user_agencia.clear() 
        except:
            self.func_aviso('Agencia invalida','OK',5)
            self.line_user_agencia.clear()
        try:
            self.password = self.line_user_senha.text()
            if len(self.password) >= 4:
                self.Password = self.password
            else:
                self.func_aviso('Senha invalida!','OK',5)
                self.line_user_senha.clear()
        except:
            ...
        def Banco_de_dados(valor1):
            banco.append(vars(valor1))
            with open(ROOT_FOLDER,'w',encoding='utf-8') as file:
                json.dump(banco,file,ensure_ascii=False,indent=2)
                
        class banco_valores:
            def __init__(self,valor1,valor2,valor3):
                self.name = valor1
                self.ag = valor2
                self.password = valor3

        if self.Name != None and self.Ag != None and self.Password != None:
            p2 = banco_valores(self.Name,self.Ag,self.Password)
            Banco_de_dados(p2)
            self.func_aviso('Cadastro realizado com Sucesso','OK',1)


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
