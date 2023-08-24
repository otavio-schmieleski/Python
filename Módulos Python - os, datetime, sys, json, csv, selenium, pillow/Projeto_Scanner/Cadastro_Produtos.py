#from Scanner import Scanner,scanner_codigo_barras
from pathlib import Path
import json
ROOT_FOLDER = Path(__file__).parent / 'Cadastro_Produtos.json'

banco = []
try:
    with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
        banco_produtos = json.load(file)
    list(banco_produtos)
except FileNotFoundError:
    pass

P_Name = None
P_Ag = None
codigo_barras = None

class Produto_name:
    def __init__(self):
        global P_Name
        # nome do produto para cadastrar
        P_Name = input("Informe o Nome do Produto ")
        if P_Name == "" or P_Name == " " or P_Name =="  " or P_Name == "   ":
            print("Informe um nome valido")
            Produto_name()
        else:
            self.name = P_Name
            print("...")


class Produto_ag:
    # agencia que o produto sera cadastrado
    def __init__(self):
        global P_Ag
        try:
            P_Ag = int(input("Informe o numero da Agencia "))
            if P_Ag >= 1 and P_Ag <= 31: 
                self.ag = P_Ag
                print("...")
        except TypeError and ValueError:
            Produto_ag()


class Produto_opcoes:
    # opcoes que serao utilizadas ou digitar ou scannear
    def __init__(self):
        global codigo_barras
        opcao = input("Deseja informar o [C]codigo de barras ou [S]Scannear")
        
        if opcao.startswith("C") or opcao.startswith("c"):
            codigo_barras = input("Informe o codigo de barras de 8 digitos ")
            if codigo_barras.isdigit() and len(codigo_barras) == 8:
                continua = True
                for codigo in banco_produtos:
                    if codigo_barras in codigo['cod_barra']:
                        print('Codigo de barras já cadastrado')
                        continua = False
                if continua == False:
                    Produto_opcoes()
                else:
                    print("Produto cadastrado com sucesso!!")
                    self.cod_barra = codigo_barras
                    pass
                         
        if opcao.startswith("S") or opcao.startswith("s"):
            #Scanner()
            for codigo in banco_produtos:
                if codigo_barras != codigo['cod_barra']:
                    print("Produto cadastrado com sucesso!!")
                    self.cod_barra = scanner_codigo_barras
                

    
# armazenando no banco de dados
def Banco_de_dados_produtos(valor):
    banco.append(vars(valor))
    with open(ROOT_FOLDER,'w',encoding='utf-8') as file:
        json.dump(banco_produtos,file,ensure_ascii=False,indent=2)


class banco_valores:
    def __init__(self,valor1,valor2,valor3):
        self.name = valor1
        self.ag = valor2
        self.cod_barra = valor3

if P_Name != None and P_Ag != None and codigo_barras != None:
    p2 = banco_valores(P_Name,P_Ag,codigo_barras)
    Banco_de_dados_produtos(p2)
