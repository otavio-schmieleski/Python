from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
from interface_user import Ui_MainWindow
import sys
from pathlib import Path
import json
from Banco_de_dados_user import Banco_de_dados_salve_user
from Banco_de_dados_prod import Banco_de_dados_save_produtos
ROOT_FOLDER = Path(__file__).parent / 'Users.json'
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'


class Window(QMainWindow,Ui_MainWindow,Banco_de_dados_salve_user,Banco_de_dados_save_produtos):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.line_altera_nome.setEnabled(False)
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
        self.btn_option_user.clicked.connect(self.btn_option_user_admin)
        self.btn_admin_procurar.clicked.connect(self.btn_admin_procura)
        self.btn_admin_alterar.clicked.connect(self.btn_alterar)
        self.btn_salve_user.clicked.connect(self.btn_salvar_alteracao_user)
        self.btn_admin_del.clicked.connect(self.btn_del_admin)
        self.btn_admin_salvar.clicked.connect(self.btn_salve_admin)
        self.btn_admin_voltar.clicked.connect(self.btn_voltar_admin)
        self.pushButton.clicked.connect(self.btn_cons_procura)
        self.btn_user_voltar.clicked.connect(self.btn_cadastro_user_volta)
        self.btn_cad_voltar.clicked.connect(self.btn_cadastro_voltar)
    
    def clicled_btn_iniciar(self):
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        self.user_informado = self.line_nome.text()
        self.password_informado = self.line_senha.text()
        continua = True
        for user in banco:
            if self.user_informado == user['name'] and self.password_informado == user['password']:
                ag = user['ag']
                continua = False
                if ag > 1:
                    self.btn_cadastro_user.setEnabled(False)
                    self.btn_option_cadastrar.setEnabled(False)
                    self.btn_option_transferir.setEnabled(False)
                    self.btn_option_user.setEnabled(False)
                else:
                    ...
                
        if continua == False:
            self.stack_pags.setCurrentIndex(1)
        else:
            self.func_aviso('Usuario ou senha incorreto!!!', 'OK','red',0)
    
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
                        self.func_aviso('Trasnferencia feita com Sucesso!!','OK','green',1)
                except TypeError and ValueError:
                    self.func_aviso('Informe uma agencia valida','OK','red',2)
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
                self.tlabe_consulta.setRowCount(len(banco_produtos) + 1)
                self.tlabe_consulta.setColumnCount(4)
                self.tlabe_consulta.setItem(0,0,QTableWidgetItem('PRODUTOS'))
                self.tlabe_consulta.setItem(0,1,QTableWidgetItem('AGENCIA'))
                self.tlabe_consulta.setItem(0,2,QTableWidgetItem('COD DE BARRAS'))
                self.tlabe_consulta.setItem(0,3,QTableWidgetItem('DATA'))
                
                try:
                    if ag > 1:
                        for i,item in enumerate(banco_produtos):
                            if ag == item['ag']:
                                self.tlabe_consulta.setItem(i+1,0,QTableWidgetItem(item['name']))
                                self.tlabe_consulta.setItem(i+1,1,QTableWidgetItem(str(item['ag'])))
                                self.tlabe_consulta.setItem(i+1,2,QTableWidgetItem(item['cod_barra']))
                                self.tlabe_consulta.setItem(i+1,3,QTableWidgetItem(item['date']))
                    else:
                        for i,item in enumerate(banco_produtos):
                            self.tlabe_consulta.setItem(i+1,0,QTableWidgetItem(item['name']))
                            self.tlabe_consulta.setItem(i+1,1,QTableWidgetItem(str(item['ag'])))
                            self.tlabe_consulta.setItem(i+1,2,QTableWidgetItem(item['cod_barra']))
                            self.tlabe_consulta.setItem(i+1,3,QTableWidgetItem(item['date']))
                except:
                    self.func_aviso('Nada de Imobilizados','OK','red',1)

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
    
    def btn_cons_procura(self):
        texto = self.lineEdit.text()
        with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
            banco_produtos = json.load(file)
        list(banco_produtos)
        self.tlabe_consulta.clear()
        self.tlabe_consulta.setRowCount(len(banco_produtos) + 1)
        self.tlabe_consulta.setColumnCount(4)
        self.tlabe_consulta.setItem(0,0,QTableWidgetItem('PRODUTOS'))
        self.tlabe_consulta.setItem(0,1,QTableWidgetItem('AGENCIA'))
        self.tlabe_consulta.setItem(0,2,QTableWidgetItem('COD DE BARRAS'))
        self.tlabe_consulta.setItem(0,3,QTableWidgetItem('DATA'))
        
        try:
            for i,item in enumerate(banco_produtos):
                if texto == item['cod_barra']:
                    self.tlabe_consulta.setItem(i+1,0,QTableWidgetItem(item['name']))
                    self.tlabe_consulta.setItem(i+1,1,QTableWidgetItem(str(item['ag'])))
                    self.tlabe_consulta.setItem(i+1,2,QTableWidgetItem(item['cod_barra']))
                    self.tlabe_consulta.setItem(i+1,3,QTableWidgetItem(item['date']))
                    
            if len(item) == 0:
                self.func_aviso('Nada de Imobilizados','OK','red',1)
        except:
            self.func_aviso('Nada de Imobilizados','OK','red',1)

    def btn_cons_salvar_banco(self):
        self.func_aviso('Salvo com Sucesso!','OK','green',1)
    
    def btn_cons_voltar_inicio(self):
        self.stack_pags.setCurrentIndex(1)

    def btn_cadastro_inicio(self):
        self.stack_pags.setCurrentIndex(4)
    
    def btn_cadastro_voltar(self):
        self.stack_pags.setCurrentIndex(1)

    def btn_cadastro_user_volta(self):
        self.stack_pags.setCurrentIndex(1)

    def btn_cadastrar_produtos(self):
        self.name = None
        self.ag = None
        self.cod_barra = None
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        # nome do produto para cadastrar
        P_Name = self.line_cad_nome_produto.text()
        if P_Name == "" or P_Name == " " or P_Name =="  " or P_Name == "   ":
            self.func_aviso('Informe um nome valido','OK','red',4)
            self.line_cad_nome_produto.clear()
        else:
            self.name = P_Name
        try:
            P_Ag = int(self.line_cad_agencia.text())
            if P_Ag >= 1 and P_Ag <= 31: 
                self.ag = P_Ag
        except TypeError and ValueError:
            self.func_aviso('Informe uma agencia valida','OK','red',4)
            self.line_cad_agencia.clear()
        codigo_barras = self.line_cad_cod_barras.text()
        if codigo_barras.isdigit() and len(codigo_barras) == 8:
            continua = True
            for codigo in banco_produtos:
                if codigo_barras in codigo['cod_barra']:
                    continua = False
            if continua == False:
                self.func_aviso('Informe um codigo de barras valido','OK','red',4)
                self.line_cad_cod_barras.clear()
            else:
                self.cod_barra = codigo_barras
                pass
        Banco_de_dados_save_produtos(self.name,self.ag,self.cod_barra)
        self.func_aviso('Cadastro realizado com Sucesso','OK','green',1)


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
            self.func_aviso('Usuario ja cadastrado','OK','red',5)
            self.line_user_nome.clear()
        else:
            self.Name = self.name
        try:
            self.ag = int(self.line_user_agencia.text())
            if self.ag >= 1 and self.ag <= 31:
                self.Ag = self.ag
            else:
                self.func_aviso('Agencia invalida','OK','red',5)
                self.line_user_agencia.clear() 
        except:
            self.func_aviso('Agencia invalida','OK','red',5)
            self.line_user_agencia.clear()
        try:
            self.password = self.line_user_senha.text()
            if len(self.password) >= 4:
                self.Password = self.password
            else:
                self.func_aviso('Senha invalida!','OK','red',5)
                self.line_user_senha.clear()
        except:
            ...
        Banco_de_dados_salve_user(self.Name,self.Ag,self.Password)
        self.func_aviso('Cadastro realizado com Sucesso','OK','green',0)

    def btn_admin_procura(self):
        self.line_admin_procurar.setPlaceholderText('Informe o nome a procurar')
        self.procurado = self.line_admin_procurar.text()
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        self.list_admin_user.clear()
        self.list_admin_user.setRowCount(len(banco) + 1)
        self.list_admin_user.setColumnCount(4)
        self.list_admin_user.setItem(0,0,QTableWidgetItem('PRODUTOS'))
        self.list_admin_user.setItem(0,1,QTableWidgetItem('AGENCIA'))
        self.list_admin_user.setItem(0,2,QTableWidgetItem('PASSWORD'))
        self.list_admin_user.setItem(0,3,QTableWidgetItem('DATA'))
        
        for i,usuario in enumerate(banco):
            if self.procurado == usuario['name']:
                item = usuario
                self.list_admin_user.setItem(i+1,0,QTableWidgetItem(item['name']))
                self.list_admin_user.setItem(i+1,1,QTableWidgetItem(str(item['ag'])))
                self.list_admin_user.setItem(i+1,2,QTableWidgetItem(item['password']))
                self.list_admin_user.setItem(i+1,3,QTableWidgetItem(item['date']))
                


    def btn_option_user_admin(self):
        self.stack_pags.setCurrentIndex(9)
        with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
            banco = json.load(file)
        list(banco)
        self.list_admin_user.setRowCount(len(banco) + 1)
        self.list_admin_user.setColumnCount(4)
        self.list_admin_user.setItem(0,0,QTableWidgetItem('PRODUTOS'))
        self.list_admin_user.setItem(0,1,QTableWidgetItem('AGENCIA'))
        self.list_admin_user.setItem(0,2,QTableWidgetItem('PASSWORD'))
        self.list_admin_user.setItem(0,3,QTableWidgetItem('DATA'))
        
        try:
            for i,item in enumerate(banco):
                self.list_admin_user.setItem(i+1,0,QTableWidgetItem(item['name']))
                self.list_admin_user.setItem(i+1,1,QTableWidgetItem(str(item['ag'])))
                self.list_admin_user.setItem(i+1,2,QTableWidgetItem(item['password']))
                self.list_admin_user.setItem(i+1,3,QTableWidgetItem(item['date']))
                
        except:
            pass

    def btn_alterar(self):
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        self.selecionado = self.list_admin_user.currentRow()
        self.alterar = banco[self.selecionado -1 ]
        self.line_altera_nome.setText(self.alterar['name'])
        self.line_altera_ag.setText(str(self.alterar['ag']))
        self.line_altera_senha.setText(self.alterar['password'])
        self.stack_pags.setCurrentIndex(8)
    
    def btn_salvar_alteracao_user(self):
        self.Name = None 
        self.Ag = None 
        self.Password = None 
        with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
            banco = json.load(file)
        list(banco)
        self.name = self.line_altera_nome.text()
        continua = True
        for usuario in banco:
            if self.name == "" or self.name == " " or self.name =="  " or self.name == "   ":
                continua = False
        if continua == False:
            self.func_aviso('Usuario ja cadastrado','OK','red',8)
        else:
            self.Name = self.name
        try:
            self.ag = int(self.line_altera_ag.text())
            if self.ag >= 1 and self.ag <= 31:
                self.Ag = self.ag
            else:
                self.func_aviso('Agencia invalida','OK','red',8)
        except:
            self.func_aviso('Agencia invalida','OK','red',8)
        try:
            self.password = self.line_altera_senha.text()
            if len(self.password) >= 4:
                self.Password = self.password
            else:
                self.func_aviso('Senha invalida!','OK','red',8)
        except:
            ...
        del banco[self.selecionado - 1]
        with open(ROOT_FOLDER, 'w', encoding='utf-8') as file:
            json.dump(banco,file,ensure_ascii=False,indent=2)
        Banco_de_dados_salve_user(self.Name,self.Ag,self.Password)
        self.btn_option_user_admin()
        
    
    def btn_del_admin(self):
        selecao = self.list_admin_user.currentRow()
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        del banco[selecao - 1]
        with open(ROOT_FOLDER, 'w', encoding='utf-8') as file:
            json.dump(banco,file,ensure_ascii=False,indent=2)
        self.btn_option_user_admin()

    def btn_salve_admin(self):
        self.func_aviso('Salvo com Sucesso!','OK','green',1)
    
    def btn_voltar_admin(self):
        self.stack_pags.setCurrentIndex(1)

    def func_aviso(self,mensagem,text_button,color,id_pags):
        self.stack_pags.setCurrentIndex(7)
        self.label_aviso.setText(f'{mensagem}')
        self.label_aviso.setStyleSheet(f'font-size: 14px; color: {color};')
        self.btn_aviso.setText(f'{text_button}')
        self.btn_aviso.clicked.connect(self.clicled_btn_aviso)
        self.id_pag = id_pags

    def clicled_btn_aviso(self):
        self.line_nome.setText('')
        self.line_senha.setText('')
        self.stack_pags.setCurrentIndex(self.id_pag)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
