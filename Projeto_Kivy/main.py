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
            View_aviso('view_inicial')
            
        

class View_principal_user(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_principal_user,self).__init__(**kwargs)
        view_consulta_user = self.ids.btn_option_consultar_user
        view_consulta_user.on_press = self.tela_consulta_user
        view_conferencia = self.ids.btn_option_conferencia
        view_conferencia.on_press = self.tela_conferencia

    def tela_consulta_user(self):
        self.manager.current = 'view_consulta'
    
    def tela_conferencia(self):
        self.manager.current = 'view_conferencia'


class View_principal(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_principal,self).__init__(**kwargs)
        view_transferir = self.ids.btn_option_transferir
        view_transferir.on_press = self.tela_transferencia
        view_consulta = self.ids.btn_option_consultar
        view_consulta.on_press = self.tela_consulta
        view_cadsatrar = self.ids.btn_option_cadastrar
        view_cadsatrar.on_press = self.tela_cadastrar
        view_cadastro_user = self.ids.btn_option_cadastro_user
        view_cadastro_user.on_press = self.tela_cadastro_user
        view_admin = self.ids.btn_admin
        view_admin.on_press = self.tela_admin

    def tela_transferencia(self):
        self.manager.current = 'view_transferencia'
    def tela_consulta(self):
        self.manager.current = 'view_consulta'
    def tela_cadastrar(self):
        self.manager.current = 'view_cadastro'
    def tela_cadastro_user(self):
        self.manager.current = 'view_user_cadastro'
    def tela_admin(self):
        self.manager.current = 'view_admin'

class View_transferencia(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_transferencia,self).__init__(**kwargs)
        btn_transferir = self.ids.btn_transf_ok
        btn_transferir.on_press = self.tela_transferir_ag
    
    def tela_transferir_ag(self):
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        self.codigo_barras = self.ids.linha_cod_barra
        for codigo in  banco_produtos:
            if self.codigo_barras.text == codigo['cod_barra']:
                self.codg = codigo['ag']
                self.manager.current = 'view_transferencia_ag'
            else:
                continue

class View_transferencia_ag(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_transferencia_ag,self).__init__(**kwargs)
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        self.codigo_barras = self.ids.linha_cod_barra
        self.line_trans_ag = self.ids.line_transf_ag
        for codigo in  banco_produtos:
            if self.codigo_barras.text == codigo['cod_barra']:
                try:
                    Ag = int(self.line_trans_ag.text)
                    if Ag >= 1 and Ag <= 31: 
                        self.ag = Ag
                        codigo['ag'] = self.ag
                        with open(ROOT_FOLDER_PRODUTOS, 'w', encoding='utf-8') as file:
                            json.dump(banco_produtos,file,ensure_ascii=False,indent=2)
                        View_sucesso()
                except TypeError and ValueError:
                    self.func_aviso('Informe uma agencia valida','OK','red',2)
                    pass

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
    def __init__(self,**kwargs):
        super(View_aviso,self).__init__(**kwargs)
        self.label_aviso = self.ids.label_aviso
        self.btn_aviso = self.ids.btn_aviso
        self.label_aviso.text = f'Ocorreu um erro'
        self.btn_aviso.on_press = self.clicled_btn_aviso

    def clicled_btn_aviso(self):
        self.manager.current = 'view_inicial'

class View_sucesso(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_sucesso,self).__init__(**kwargs)
        self.label_sucesso = self.ids.label_sucesso
        self.btn_sucesso = self.ids.btn_sucesso
        self.label_sucesso.text = f'Concluida com Sucesso'
        self.btn_sucesso.on_press = self.clicled_btn_aviso

    def clicled_btn_aviso(self):
        self.manager.current = 'view_principal'

class View_alterar_usuario(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_alterar_usuario,self).__init__(**kwargs)

class View_admin(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_admin,self).__init__(**kwargs)

class View_conferencia(Screen,FloatLayout):
    def __init__(self, **kw):
        super(View_conferencia,self).__init__(**kw)
        
class interface_user(App):
    def build(self):
        self.title = "CONTROLE DE IMOBILIZADOS"
        self.sm = ScreenManager()
        self.sm.add_widget(View_inicial(name = 'view_inicial'))
        self.sm.add_widget(View_admin(name = 'view_admin'))
        self.sm.add_widget(View_alterar_usuario(name = 'view_altera_usuario'))
        self.sm.add_widget(View_aviso(name = 'view_aviso'))
        self.sm.add_widget(View_cadastro(name = 'view_cadastro'))
        self.sm.add_widget(View_consulta(name = 'view_consulta'))
        self.sm.add_widget(View_principal(name = 'view_principal'))
        self.sm.add_widget(View_principal_user(name = 'view_principal_user'))
        self.sm.add_widget(View_transferencia(name = 'view_transferencia'))
        self.sm.add_widget(View_transferencia_ag(name = 'view_transferencia_ag'))
        self.sm.add_widget(View_user_cadastro(name = 'view_user_cadastro'))
        self.sm.add_widget(View_conferencia(name='view_conferencia'))
        self.sm.add_widget(View_sucesso(name='view_sucesso'))
        
        return self.sm

window = interface_user()
window.run()