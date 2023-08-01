import random
import json
CAMINHO_ARQUIVO = 'C:\\Users\\otavi\\OneDrive\\Documentos\\Programacao-fullstack\\Python\\Orientacao_Objeto\\sistema_bancario\\cadastro.json'

with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
    banco = json.load(arquivo)
   

class Cadastro():
    def __init__(self) :
        Criar_Conta()
        try:
            self.nome = input('Informe seu Nome: ')
            if self.nome != '' and self.nome != ' ':
                ...
        except:
            print('Informe um Nome Valido')
            Cadastro()
        try:
            self.rg = (input('Informe seu rg: '))
            if len(self.rg) == 8 and self.rg.isdigit():
                ...
        except:
            print('Informe um Rg valido')
            Cadastro()

        try:
            self.cpf= input('Informe seu cpf: ')
            if len(self.cpf) == 11 :
                ...
        except:
            print('Informe um cpf Valido')
            Cadastro()
        try:
            self.idade = input('Informe seu idade: ')
            if self.idade.isdigit():
                ...
        except:
            print('Informe uma Idade Valida')
            Cadastro()
        try:
            self.sexo = input('Informe seu sexo: ')
            if self.sexo != '' and self.sexo != ' ':
                ...
        except:
            print('Informe um sexo valido ou [M]masculino ou [F]femenino')
            Cadastro()
        self.conta = contas
        try:
            self.saldo = float(input('Informe seu valor de Deposito Inicial: R$ '))
        except:
            print('informe um valor válido')
            Cadastro()


        
        def Printar():
            print(f'Nome: {self.nome}')
            print(f'RG: {self.rg}')
            print(f'CPF: {self.cpf}')
            print(f'IDADE: {self.idade}')
            print(f'SEXO: {self.sexo}')
            print(f'CONTA: {self.conta}')
            print(f'SALDO: {float(self.saldo)}')
        Printar()

def Criar_Conta():
    global contas 
    contas = ''
    numero = random.randrange(9)
    numero1 = random.randrange(9)
    numero2 = random.randrange(9)
    contas = str(numero)+str(numero1)+str(numero2)

def Banco_de_Dados(item):
    banco.append(vars(item))
    with open(CAMINHO_ARQUIVO,'w',encoding='utf8') as arquivo:
        json.dump(banco,arquivo,ensure_ascii=False,indent=2)
            


