from pathlib import Path
import json
from datetime import datetime
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'

banco = []
try:
    with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
        banco_produtos = json.load(file)
    list(banco_produtos)
except FileNotFoundError:
    pass

class Banco_de_dados_save_produtos():
    def __init__(self,name,ag,cod_barra):
        self.P_Name = name
        self.P_Ag = ag
        self.codigo_barras = cod_barra
        self.data = datetime.today().strftime("%d/%m/%y - %H:%M:%S")

        if self.P_Name != None and self.P_Ag != None and self.codigo_barras != None:
            p2 = self.banco_valores(self.P_Name,self.P_Ag,self.codigo_barras,self.data)
            self.Banco_de_dados_produtos(p2)

    def Banco_de_dados_produtos(self,valor):
        banco_produtos.append(vars(valor))
        with open(ROOT_FOLDER_PRODUTOS,'w',encoding='utf-8') as file:
            json.dump(banco_produtos,file,ensure_ascii=False,indent=2)

    class banco_valores:
        def __init__(self,valor1,valor2,valor3,valor4):
            self.name = valor1
            self.ag= valor2
            self.cod_barra = valor3
            self.date = valor4