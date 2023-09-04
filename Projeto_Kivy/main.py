import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.app import App
from pathlib import Path
import json

ROOT_FOLDER = Path(__file__).parent / 'Users.json'
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'
ROOT_FOLDER_TEMP = Path(__file__).parent / 'temp.json'


class View_inicial(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_inicial,self).__init__(**kwargs)
        btn_inicial = self.ids.btn_inicial
        btn_inicial.on_press = self.click_btn_inicial

    def click_btn_inicial(self):
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        self.user_informado = self.ids.line_nome.text
        self.password_informado = self.ids.line_senha.text
        continua = True
        for user in banco:
            if self.user_informado == user['name'] and self.password_informado == user['password']:
                self.agencia = user['ag']
                continua = False
                
        if continua == False:
            if self.agencia > 1:
                self.manager.current = 'view_principal_user'
            else:
                self.manager.current = 'view_principal'
        else:
            self.manager.current = 'view_aviso'
            View_aviso('Usuario ou senha incorreto!!!','view_inicial')
            
        

class View_principal_user(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_principal_user,self).__init__(**kwargs)

class View_principal(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_principal,self).__init__(**kwargs)

class View_transferencia(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_transferencia,self).__init__(**kwargs)

class View_transferencia_ag(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_transferencia_ag,self).__init__(**kwargs)

class View_cadastro(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_cadastro,self).__init__(**kwargs)

class View_user_cadastro(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_user_cadastro,self).__init__(**kwargs)

class View_consulta(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_consulta,self).__init__(**kwargs)

class View_aviso(Screen,FloatLayout):
    def __init__(self, mensagem: None,id:None,**kwargs):
        super(View_aviso,self).__init__(**kwargs)
        self.label_aviso = self.ids.label_aviso
        self.btn_aviso = self.ids.btn_aviso
        self.label_aviso.text = f'{mensagem}'
        self.id = id
        self.btn_aviso.on_press = self.clicled_btn_aviso

    def clicled_btn_aviso(self):
        self.manager.current = 'view_inicial'


class View_alterar_usuario(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_alterar_usuario,self).__init__(**kwargs)

class View_admin(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_admin,self).__init__(**kwargs)

        
class interface_user(App):
    def build(self):
        self.title = "CONTROLE DE IMOBILIZADOS"
        self.sm = ScreenManager()
        self.sm.add_widget(View_inicial(name = 'view_inicial'))
        self.sm.add_widget(View_admin(name = 'view_admin'))
        self.sm.add_widget(View_alterar_usuario(name = 'view_altera_usuario'))
        self.sm.add_widget(View_aviso(mensagem='',id='',name = 'view_aviso'))
        self.sm.add_widget(View_cadastro(name = 'view_cadastro'))
        self.sm.add_widget(View_consulta(name = 'view_consulta'))
        self.sm.add_widget(View_principal(name = 'view_principal'))
        self.sm.add_widget(View_principal_user(name = 'view_principal_user'))
        self.sm.add_widget(View_transferencia(name = 'view_transferencia'))
        self.sm.add_widget(View_transferencia_ag(name = 'view_transferencia_ag'))
        self.sm.add_widget(View_user_cadastro(name = 'view_user_cadastro'))
        
        return self.sm

window = interface_user()
window.run()