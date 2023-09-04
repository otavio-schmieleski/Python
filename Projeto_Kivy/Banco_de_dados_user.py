from pathlib import Path
import json
from datetime import datetime

ROOT_FOLDER = Path(__file__).parent / 'Users.json'


class Banco_de_dados_salve_user():
    def __init__(self,name,ag,password):
        with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
            self.banco = json.load(file)
        list(self.banco)
        self.Name = name
        self.Ag = ag
        self.Password = password
        self.data = datetime.today().strftime("%d/%m/%y - %H:%M:%S")
        
        if self.Name != None and self.Ag != None and self.Password != None:
            p2 = self.banco_valores(self.Name,self.Ag,self.Password,self.data)
            self.Banco_de_dados(p2)

    def Banco_de_dados(self,valor1):
        self.banco.append(vars(valor1))
        with open(ROOT_FOLDER,'w',encoding='utf-8') as file:
            json.dump(self.banco,file,ensure_ascii=False,indent=2)
          
    class banco_valores():
        def __init__(self,valor1,valor2,valor3,valor4):
            self.name = valor1
            self.ag = valor2
            self.password = valor3
            self.date = valor4