import json
from pathlib import Path
ROOT_FOLDER = Path(__file__).parent / 'Users.json'

banco = []
try:
    with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
        banco = json.load(file)
    list(banco)
except FileNotFoundError:
    pass

name = None
ag = None
password = None
class User_name:
    def __init__(self,nome):
        global name
        name = nome
        continua = True
        for usuario in banco:
            if name == usuario['name'] or name == "" or name == " " or name =="  " or name == "   ":
                print('Usuario ja cadastrado')
                continua = False
        if continua == False:
            User_name(nome)
        else:
            self.name = name

class User_ag:
    def __init__(self,agencia):
        global ag
        try:
            ag = int(agencia)
            if ag >= 1 and ag <= 31:
                self.ag = ag
            else:
                print('Agencia invalida')
                User_ag(agencia) 
        except:
            print('Informe uma agencia valida!')
            User_ag()

class User_password:
    def __init__(self,senha):
        global password
        try:
            password = senha
            if len(password) >= 4:
                self.password = password
            else:
                User_password(senha)
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

if name != None and ag != None and password != None:
    p2 = banco_valores(name,ag,password)
    Banco_de_dados(p2)