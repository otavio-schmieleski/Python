import os
import sys
import time
from PySide6.QtWidgets import QApplication,QMainWindow
from interface_user import Ui_MainWindow
from Autentic_User import Autentic,Banco_de_dados,User_ag,User_name,User_password,banco_valores,name,ag,password
# while True:
#     os.system('cls')
#     print("CONTROLE DE IMOBILIZADOS!")
#     opcao = input('Deseja fazer [L]Login ou [C]Cadastrar-se ')
#     if opcao.startswith('L') or opcao.startswith('l'):
#         Autentic()
#     elif opcao.startswith('C') or opcao.startswith('c'):
#         p1 = User_name(),User_ag(),User_password()

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.stack_pags.setCurrentIndex(0)
        self.line_senha.setEchoMode(self.line_senha.EchoMode.Password)
        self.btn_inicial.clicked.connect(self.btn_clicled_iniciar)
        self.btn_cadastro_user.clicked.connect(self.btn_clicled_cadastro_inicial)
        self.btn_user_cadastrar.clicked.connect(self.btn_cliced_cadastro_user)
        
    
    def btn_clicled_iniciar(self):
        Autentic(self.line_nome.text(),self.line_senha.text())
        if continua == False:
            self.stack_pags.setCurrentIndex(1)
        else:
            self.create_aviso('usuario o senha invalidos !!')

    def btn_clicled_cadastro_inicial(self):
        self.stack_pags.setCurrentIndex(5)
    
    def btn_cliced_cadastro_user(self):
        p1 = User_name(self.line_user_nome.text()), User_ag(self.line_user_agencia.text()),
        User_password(self.line_user_senha.text())
    
    def create_aviso(self,mensagem):
        self.label_aviso.setText(f"{mensagem}")
        self.label_aviso.setGeometry(55,45,311,121)
        self.label_aviso.setStyleSheet('font-size: 18px; text-align: center; color: red')
        self.btn_aviso.setText('OK')
        self.stack_pags.setCurrentIndex(7)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())

