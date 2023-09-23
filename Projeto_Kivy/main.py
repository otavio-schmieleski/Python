import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from pathlib import Path
import json
from kivy.config import Config
from Banco_de_dados_prod import Banco_de_dados_save_produtos
from Banco_de_dados_user import Banco_de_dados_salve_user
#from Envio_de_Email import Email_Automatico

#Config.set('graphics', 'icon', 'logo.png')
kivy.require('2.2.1')
ROOT_FOLDER = Path(__file__).parent / 'Users.json'
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'
ROOT_FOLDER_TEMP = Path(__file__).parent / 'temp.json'
ROOT_FOLDER_TEMP_PROCURA = Path(__file__).parent / 'Temp_procura.json'
ROOT_FOLDER_LOG = Path(__file__).parent / 'Log.json'

lista_de_conferencia = []
user_nome = ''
user_agencia = 0
# Tela Inicial
class View_inicial(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_inicial,self).__init__(**kwargs)
        btn_inicial = self.ids.btn_inicial
        btn_inicial.on_press = self.click_btn_inicial

    # funcao do clique do botao entrar da tela inicial
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
        # vereficacao para saber se fechou as informacoes com o banco de dados
        for user in banco:
            if self.user_informado == user['name'] and self.password_informado == user['password']:
                self.agencia = user['ag']
                log = user
                with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
                    log_banco = json.load(file)
                list(log_banco)
                log_banco.append(log)
                with open(ROOT_FOLDER_LOG,'w',encoding='utf-8') as file:
                    json.dump(log_banco,file,ensure_ascii=False,indent=2)
                continua = False
                
        if continua == False:
            if self.agencia > 1:
                with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                    banco_produtos = json.load(file)
                list(banco_produtos)
                lista_produto = []
                for ag in banco_produtos:
                    if self.agencia == ag['ag']:
                        produto = ag
                        lista_produto.append(produto)
                    else:
                        continue
                with open(ROOT_FOLDER_TEMP_PROCURA, 'w', encoding='utf-8') as file:
                    json.dump(lista_produto,file,ensure_ascii=False,indent=2)

                with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
                    log_banco = json.load(file)
                list(log_banco)
                del log_banco[0]
                with open(ROOT_FOLDER_LOG,'w',encoding='utf-8') as file:
                    json.dump(log_banco,file,ensure_ascii=False,indent=2)

                self.manager.current = 'view_principal_user'

            else:
                with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                    banco_produtos = json.load(file)
                list(banco_produtos)
                lista_produto = []
                for item in banco_produtos:
                    lista_produto.append(item)
                with open(ROOT_FOLDER_TEMP_PROCURA, 'w', encoding='utf-8') as file:
                    json.dump(lista_produto,file,ensure_ascii=False,indent=2)
                with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
                    log_banco = json.load(file)
                list(log_banco)
                del log_banco[0]
                with open(ROOT_FOLDER_LOG,'w',encoding='utf-8') as file:
                    json.dump(log_banco,file,ensure_ascii=False,indent=2)
                self.manager.current = 'view_principal'
        else:
            self.manager.current = 'view_aviso_inicial'
            View_aviso_inicial()
            
        

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
        btn_transferir = self.ids.btn_transferir
        btn_transferir.on_press = self.tela_transferir_ag
        btn_volta = self.ids.btn_transf_voltar
        btn_volta.on_press = self.tela_voltar
    
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
                self.line_trans_ag = self.ids.line_transf_ag
                try:
                    Ag = int(self.line_trans_ag.text)
                    if Ag >= 1 and Ag <= 31: 
                        self.ag = Ag
                        codigo['ag'] = self.ag
                        with open(ROOT_FOLDER_PRODUTOS, 'w', encoding='utf-8') as file:
                            json.dump(banco_produtos,file,ensure_ascii=False,indent=2)
                        self.codigo_barras.text = ''
                        self.line_trans_ag.text = ''
                        self.manager.current = 'view_sucesso'
                        View_sucesso()

                except TypeError and ValueError:
                    self.manager.current = 'view_aviso'
                    View_aviso()
                    pass
            else:
                continue
        else:
            self.manager.current = 'view_aviso_admin'
            View_aviso_admin()
        
    def tela_voltar(self):
        self.manager.current = 'view_principal'

class View_cadastro(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_cadastro,self).__init__(**kwargs)
        btn_cadastro = self.ids.btn_cadastrar
        btn_cadastro.on_press = self.btn_cadastrar
        btn_voltar = self.ids.btn_cad_voltar
        btn_voltar.on_press = self.btn_voltar
    def btn_cadastrar (self):
        self.name_produto = None
        self.ag = None
        self.cod_barra = None
        try:
            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        # nome do produto para cadastrar
        P_Name = self.ids.line_cad_nome_produto.text
        if P_Name == "" or P_Name == " " or P_Name =="  " or P_Name == "   ":
            self.manager.current = 'view_aviso'
            View_aviso()
        else:
            self.name_produto = P_Name
        try:
            P_Ag = int(self.ids.line_cad_agencia.text)
            if P_Ag >= 1 and P_Ag <= 31: 
                self.ag = P_Ag
        except TypeError and ValueError:
            self.manager.current = 'view_aviso'
            View_aviso()
        codigo_barras = self.ids.line_cad_cod_barras.text
        if codigo_barras.isdigit() and len(codigo_barras) == 8:
            continua = True
            for codigo in banco_produtos:
                if codigo_barras in codigo['cod_barra']:
                    continua = False
            if continua == False:
                self.manager.current = 'view_aviso'  
                View_aviso()
            else:
                self.cod_barra = codigo_barras
                pass
        Banco_de_dados_save_produtos(self.name_produto,self.ag,self.cod_barra)
        self.manager.current = 'view_sucesso'
        View_sucesso()

    def btn_voltar(self):
        self.manager.current = 'view_principal'


class View_user_cadastro(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_user_cadastro,self).__init__(**kwargs)
        btn_cadastrar_user = self.ids.btn_user_cadastrar
        btn_cadastrar_user.on_press = self.btn_cadastro_user
        btn_voltar = self.ids.btn_user_voltar
        btn_voltar.on_press = self.btn_voltar_tela

    def btn_cadastro_user(self):
        self.Name_user = None
        self.Ag = None
        self.Password = None
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        self.name = self.ids.line_user_nome.text
        continua = True
        for usuario in banco:
            if self.name == usuario['name'] or self.name == "" or self.name == " " or self.name =="  " or self.name == "   ":
                continua = False
        if continua == False:
            self.manager.current = 'view_aviso_admin'  
            View_aviso_admin()
        else:
            self.Name_user = self.name
        try:
            self.ag = int(self.ids.line_user_agencia.text)
            if self.ag >= 1 and self.ag <= 31:
                self.Ag = self.ag
            else:
                self.manager.current = 'view_aviso_admin'  
                View_aviso_admin()
        except:
            self.manager.current = 'view_aviso_admin'  
            View_aviso_admin()
        try:
            self.password = self.ids.line_user_senha.text
            if len(self.password) >= 4:
                self.Password = self.password   
            else:
                self.manager.current = 'view_aviso_admin'  
                View_aviso_admin()
        except:
            self.manager.current = 'view_aviso_admin'  
            View_aviso_admin()
            
        Banco_de_dados_salve_user(self.Name_user,self.Ag,self.Password)
        self.manager.current = 'view_sucesso'
        View_sucesso()
        
    def btn_voltar_tela(self):
        self.manager.current = 'view_principal'

class View_consulta(Screen,FloatLayout,GridLayout,Label):
    def __init__(self, **kwargs):
        super(View_consulta,self).__init__(**kwargs)
        self.line_procura = self.ids.line_cons_procurar.text
        self.lb_nome_produto = self.ids.lb_produto_nome
        self.lb_produto_ag = self.ids.lb_produto_agencia
        self.lb_produto_cod = self.ids.lb_cod_barra
        self.btn_voltar = self.ids.btn_cons_voltar
        self.btn_voltar.on_press = self.tela_voltar
        self.btn_salvar = self.ids.btn_cons_salvar
        self.btn_salvar.on_press = self.tela_salvar
        self.btn_procura = self.ids.btn_cons_procurar
        self.btn_procura.on_press = self.consulta
        self.btn_deletar = self.ids.btn_cons_excluir
        self.btn_deletar.on_press = self.deletar_produto
        self.btn_deletar = self.ids.btn_cons_excluir
        self.btn_deletar.on_press = self.deletar_produto
        with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
            log_banco = json.load(file)
        list(log_banco)
        for user in log_banco:
            if user['ag'] == 1:
                self.btn_deletar.disabled = True
            else:
                self.btn_deletar.disabled = False

    def consulta(self):
        try:
            with open(ROOT_FOLDER_PRODUTOS,'r',encoding='utf-8') as file:
                banco = json.load(file)
            list (banco)
        except:
            ...

        for produtos in banco:
            line_procura = self.ids.line_cons_procurar.text
            if line_procura in produtos['cod_barra'] and line_procura != '':
                self.lb_nome_produto.text = ''
                self.lb_produto_ag.text = ''
                self.lb_produto_cod.text = ''
                self.lb_nome_produto.text = f"PRODUTO:  {produtos['name']}".upper()
                self.lb_produto_ag.text = f"AGENCIA:  {str(produtos['ag'])}"
                self.lb_produto_cod.text = f"COD_BARRA:  {produtos['cod_barra']}"
            elif line_procura == '':
                with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
                    log_banco = json.load(file)
                list(log_banco)
                for user in log_banco:
                    if user['ag'] != 1:
                        self.manager.current = 'view_aviso'
                        View_aviso()
                    else:
                        self.manager.current = 'view_aviso_admin'
                        View_aviso_admin()
            else:
                continue
    
    def tela_voltar(self):
        with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
            log_banco = json.load(file)
        list(log_banco)
        for user in log_banco:
            if user['ag'] != 1:
                self.manager.current = 'view_principal_user'
                self.lb_nome_produto.text = ''
                self.lb_produto_ag.text = ''
                self.lb_produto_cod.text = ''
            else:
                self.manager.current = 'view_principal'
                self.lb_nome_produto.text = ''
                self.lb_produto_ag.text = ''
                self.lb_produto_cod.text = ''
    
    def tela_salvar(self):
        with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
            log_banco = json.load(file)
        list(log_banco)
        for user in log_banco:
            if user['ag'] != 1:
                self.lb_nome_produto.text = ''
                self.lb_produto_ag.text = ''
                self.lb_produto_cod.text = ''
                self.manager.current = 'view_sucesso_user'
                View_sucesso_user()
            else:
                self.lb_nome_produto.text = ''
                self.lb_produto_ag.text = ''
                self.lb_produto_cod.text = ''
                self.manager.current = 'view_sucesso'
                View_sucesso()
    
    def deletar_produto(self):
        with open(ROOT_FOLDER_PRODUTOS,'r',encoding='utf-8') as file:
            banco = json.load(file)
        list (banco)
        line_procura = self.ids.line_cons_procurar.text
        for i,produto in enumerate(banco):
            if line_procura in produto['cod_barra'] and line_procura != '':
                del banco[i]
                with open(ROOT_FOLDER_PRODUTOS,'w', encoding='utf-8') as file:
                    json.dump(banco,file,ensure_ascii=False,indent=2)

                with open(ROOT_FOLDER_LOG,'r',encoding='utf-8') as file:
                    log_banco = json.load(file)
                list(log_banco)
                for user in log_banco:
                    if user['ag'] != 1:
                        self.lb_nome_produto.text = ''
                        self.lb_produto_ag.text = ''
                        self.lb_produto_cod.text = ''
                        self.manager.current = 'view_sucesso_user'
                        View_sucesso_user()
                    else:
                        self.lb_nome_produto.text = ''
                        self.lb_produto_ag.text = ''
                        self.lb_produto_cod.text = ''
                        self.manager.current = 'view_sucesso'
                        View_sucesso()
            else:
                continue


class View_alterar_usuario(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_alterar_usuario,self).__init__(**kwargs)
        self.btn_procurar = self.ids.btn_alterar_procurar
        self.btn_procurar.on_press = self.alterar_procurar
        self.btn_salvar = self.ids.btn_salve_user
        self.btn_salvar.on_press = self.alterar_salvar
        self.line_nome = self.ids.line_altera_nome
        self.line_ag = self.ids.line_altera_ag
        self.line_senha = self.ids.line_altera_senha

    def alterar_procurar(self):
        self.line_procurar = self.ids.line_alterar_procurar
        procura = self.line_procurar.text
        with open(ROOT_FOLDER,'r',encoding='utf-8') as file:
            banco = json.load(file)
        list(banco)
        for user in banco:
            if procura in user['name']:
                self.line_nome.text = user['name']
                self.line_ag.text = str(user['ag'])
                self.line_senha.text = user['password']
            else:
                continue
    
    def alterar_salvar(self):
        self.Name_user = None
        self.Ag = None
        self.Password = None
        banco = []
        try:
            with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
                banco = json.load(file)
            list(banco)
        except FileNotFoundError:
            pass
        self.name = self.line_nome.text
        continua = True
        for usuario in banco:
            if self.name == "" or self.name == " " or self.name =="  " or self.name == "   ":
                continua = False
        if continua == False:
            self.manager.current = 'view_aviso'  
            View_aviso()
        else:
            self.Name_user = self.name
        try:
            self.ag = int(self.line_ag.text)
            if self.ag >= 1 and self.ag <= 31:
                self.Ag = self.ag
            else:
                self.manager.current = 'view_aviso'  
                View_aviso()
        except:
            self.manager.current = 'view_aviso'  
            View_aviso()
        try:
            self.password = self.line_senha.text
            if len(self.password) >= 4:
                self.Password = self.password   
            else:
                self.manager.current = 'view_aviso'  
                View_aviso()
        except:
            ...
        for i,nome in enumerate(banco):
            if self.line_nome.text in nome['name']:
                del banco[i]
                with open(ROOT_FOLDER, 'w', encoding='utf-8') as file:
                    json.dump(banco,file,ensure_ascii=False,indent=2)
        Banco_de_dados_salve_user(self.Name_user,self.Ag,self.Password)
        self.manager.current = 'view_sucesso'
        View_sucesso()


class View_admin(Screen,GridLayout):
    def __init__(self, **kwargs):
        super(View_admin,self).__init__(**kwargs)
        self.btn_alterar = self.ids.btn_admin_alterar
        self.btn_alterar.on_press = self.tela_alterar
        self.btn_admin_salvar = self.ids.btn_admin_salvar
        self.btn_admin_salvar.on_press = self.tela_salvar
        self.btn_admin_voltar = self.ids.btn_admin_voltar
        self.btn_admin_voltar.on_press = self.tela_voltar
        self.btn_admin_procurar = self.ids.btn_admin_procurar
        self.btn_admin_procurar.on_press = self.procurar
        self.btn_del = self.ids.btn_admin_excluir
        self.btn_del.on_press = self.deletar

    def procurar(self):
        self.lb_nome = self.ids.lb_nome
        self.lb_ag = self.ids.lb_agencia
        self.lb_senha = self.ids.lb_senha
        self.line_procura = self.ids.line_admin_procurar.text

        with open(ROOT_FOLDER,'r',encoding='utf-8') as file:
            banco = json.load(file)
        list (banco)

        for user in banco:
            if self.line_procura in user['name']:
                self.lb_nome.text = f"USUARIO:  {user['name']}".upper()
                self.lb_ag.text = f"AGENCIA:  {str(user['ag'])}"
                self.lb_senha.text = f"SENHA:  {user['password']}"
            else:
                continue
    
    def deletar(self):
        with open(ROOT_FOLDER,'r',encoding='utf-8') as file:
            banco = json.load(file)
        list (banco)

        for i,user in enumerate(banco):
            if self.line_procura in user['name'] and self.line_procura != '':
                del banco[i]
                with open(ROOT_FOLDER,'w', encoding='utf-8') as file:
                    json.dump(banco,file,ensure_ascii=False,indent=2)
                self.lb_nome.text = ''
                self.lb_ag.text = ''
                self.lb_senha.text = ''
                self.manager.current = 'view_sucesso'
                View_sucesso()
            else:
                continue

    
    def tela_alterar(self):
        self.manager.current = 'view_altera_usuario'
    
    def tela_salvar(self):
        self.manager.current = 'view_sucesso'
        View_sucesso()
    
    def tela_voltar(self):
        self.manager.current = 'view_principal'

        

class View_conferencia(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_conferencia,self).__init__(**kwargs)
        btn_conferir = self.ids.btn_conferencia_procurar
        btn_conferir.on_press = self.conferencia
        btn_salvar = self.ids.btn_conferencia_salvar
        btn_salvar.on_press = self.btn_salvar_temp
        btn_finalizar = self.ids.btn_conferencia_finalizar
        btn_finalizar.on_press = self.finalizar

    def conferencia(self):
        cod_barra = self.ids.conf_cod_barra.text
        with open(ROOT_FOLDER_TEMP_PROCURA,'r',encoding='utf-8') as file:
            banco = json.load(file)
        list(banco)
        for i,produto in enumerate(banco):
            if cod_barra in produto['cod_barra']:
                item = produto
                produto = self.ids.label_produto
                produto.text = f"Produto: {item['name']}    Agencia: {item['ag']}   Cod_barra: {item['cod_barra']}"
                lista_de_conferencia.append(item)
                del banco[i]
                with open(ROOT_FOLDER_TEMP, 'w', encoding='utf-8') as file:
                    json.dump(lista_de_conferencia,file,ensure_ascii=False,indent=2)
                with open(ROOT_FOLDER_TEMP_PROCURA, 'w', encoding='utf-8') as file:
                    json.dump(banco,file,ensure_ascii=False,indent=2)
            else:
                continue
    
    def btn_salvar_temp(self):
        self.manager.current = 'view_sucesso_user'
        View_sucesso()
    
    def finalizar(self):
        #Email_Automatico('Conferencia de Imobilizados',user_nome,user_agencia)
        self.manager.current = 'view_sucesso_user'
        View_sucesso()

class View_sucesso(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_sucesso,self).__init__(**kwargs)
        self.label_sucesso = self.ids.label_sucesso
        self.btn_sucesso = self.ids.btn_sucesso
        self.label_sucesso.text = f'Concluida com Sucesso'
        self.btn_sucesso.on_press = self.clicled_btn_aviso

    def clicled_btn_aviso(self):
        self.manager.current = 'view_principal'

class View_sucesso_user(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super(View_sucesso_user,self).__init__(**kwargs)
        self.label_sucesso = self.ids.label_sucesso_user
        self.btn_sucesso = self.ids.btn_sucesso_user
        self.label_sucesso.text = f'Concluida com Sucesso'
        self.btn_sucesso.on_press = self.clicled_btn_aviso

    def clicled_btn_aviso(self):
        self.manager.current = 'view_principal_user'
        
class View_aviso_inicial(Screen,FloatLayout):
    def __init__(self,**kwargs):
        super(View_aviso_inicial,self).__init__(**kwargs)
        self.label_aviso = self.ids.label_aviso_inicial
        self.btn_aviso = self.ids.btn_aviso_inicial
        self.label_aviso.text = f'Ocorreu um erro'
        self.btn_aviso.on_press = self.clicled_btn_aviso

    def clicled_btn_aviso(self):
        self.manager.current = 'view_inicial'

class View_aviso(Screen,FloatLayout):
    def __init__(self,**kwargs):
        super(View_aviso,self).__init__(**kwargs)
        self.label_aviso = self.ids.label_aviso
        self.btn_aviso = self.ids.btn_aviso
        self.label_aviso.text = f'Ocorreu um erro'
        self.btn_aviso.on_press = self.clicled_btn_aviso

    def clicled_btn_aviso(self):
        self.manager.current = 'view_principal_user'

class View_aviso_admin(Screen,FloatLayout):
    def __init__(self,**kwargs):
        super(View_aviso_admin,self).__init__(**kwargs)
        self.label_aviso_admin = self.ids.label_aviso_admin
        self.btn_aviso_admin = self.ids.btn_aviso_admin
        self.label_aviso_admin.text = f'Ocorreu um erro'
        self.btn_aviso_admin.on_press = self.clicled_btn_aviso_admin

    def clicled_btn_aviso_admin(self):
        self.manager.current = 'view_principal'


class interface_user(App):
    def build(self):
        self.title = "CONTROLE DE IMOBILIZADOS"
        self.sm = ScreenManager()
        self.sm.add_widget(View_inicial(name = 'view_inicial'))
        self.sm.add_widget(View_admin(name = 'view_admin'))
        self.sm.add_widget(View_alterar_usuario(name = 'view_altera_usuario'))
        self.sm.add_widget(View_aviso(name = 'view_aviso'))
        self.sm.add_widget(View_aviso_inicial(name = 'view_aviso_inicial'))
        self.sm.add_widget(View_aviso_admin(name='view_aviso_admin'))
        self.sm.add_widget(View_cadastro(name = 'view_cadastro'))
        self.sm.add_widget(View_consulta(name = 'view_consulta'))
        self.sm.add_widget(View_principal(name = 'view_principal'))
        self.sm.add_widget(View_principal_user(name = 'view_principal_user'))
        self.sm.add_widget(View_transferencia(name = 'view_transferencia'))
        self.sm.add_widget(View_user_cadastro(name = 'view_user_cadastro'))
        self.sm.add_widget(View_conferencia(name='view_conferencia'))
        self.sm.add_widget(View_sucesso(name='view_sucesso'))
        self.sm.add_widget(View_sucesso_user(name='view_sucesso_user'))
        return self.sm

interface_user().run()