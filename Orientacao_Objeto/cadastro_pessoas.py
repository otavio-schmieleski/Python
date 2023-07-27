import json

banco = []
CAMINHO_ARQUIVO = 'C:\\Users\\otavi\\OneDrive\\Documentos\\Programacao-fullstack\\Python\\Orientacao_Objeto'


while True:
    class Cadastro:
        def __init__(self) :
            self.nome = input('Informe seu Nome: ')
            self.rg = input('Informe seu rg: ')
            self.cpf = input('Informe seu cpf: ')
            self.idade = input('Informe seu idade: ')
            self.sexo = input('Informe seu sexo: ')

    def Banco_de_Dados(item):
        banco.append(vars(item))
        with open(CAMINHO_ARQUIVO,'w',encoding='utf8') as arquivo:
            json.dump(banco,arquivo,ensure_ascii=False,indent=2)

    def Printar(item):
        print(f'Nome: {item.nome}')
        print(f'RG: {item.rg}')
        print(f'CPF: {item.cpf}')
        print(f'IDADE: {item.idade}')
        print(f'SEXO: {item.sexo}')

    def Listar_Usuarios_Cadastrados():
        with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo:
            print(json.load(arquivo))
        

    p1 = Cadastro()
    p2 = Cadastro()
    Banco_de_Dados(p1)
    Banco_de_Dados(p2)
    Printar(p1)
    Listar_Usuarios_Cadastrados()
