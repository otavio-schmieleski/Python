from pathlib import Path
from Options import opcao_autentic,Banco_de_dados,User_ag,User_name,User_password,banco_valores,name,ag,password
import json

ROOT_FOLDER = Path(__file__).parent / 'Users.json'

try:
    with open(ROOT_FOLDER, 'r', encoding='utf-8') as file:
        banco = json.load(file)
    list(banco)
except FileNotFoundError:
    pass

class Autentic():
    def __init__(self):
        user_informado = input("Digite o nome do usuario: ")
        password_informado = input("Digite a senha: ")
        continua = True
        for user in banco:
            if user_informado == user['name'] and password_informado == user['password']:
                continua = False
        if continua == False:
            opcao_autentic(user_informado)
        else:
            print("Usuario ou senha incorreto!!! \n")
            opcao = input("Deseja [T]tentar novamente ou [C]cadastrar Usuario")
            if opcao.startswith('T') or opcao.startswith('t'):
                Autentic()
            elif opcao.startswith('C') or opcao.startswith('c'):
                p1 = User_name(),User_ag(),User_password()
            else:
                print("Nenhuma opcao valída !!!!")
                Autentic()