import json
from pathlib import Path
ROOT_FOLDER = Path(__file__).parent / 'Users.json'

#with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
#    file = json.load(file)
#list(file)

class Record_User:
    def __init__(self):
        def Name():
            Name = input("Informe seu Nome ")
            if Name == "" or Name == " " or Name =="  " or Name == "   ":
                print("Informe um nome valido")
                Record_User()
            else:
                self.name = Name
                print("...")
            
        def Ag():
            try:
                Ag = int(input("Informe o numero da Agencia "))
                if Ag >= 1 and Ag <= 31: 
                    self.ag = Ag
                    print("...")
            except TypeError and ValueError:
                Record_User()
            
        def Password():
            password = input("Informe uma senha de 4 digitos ")
            if len(password) >= 4:
                self.password = password
            else:
                Record_User()
        
        Name()
        Ag()
        Password()
        

Record_User()