import json

banco_dados = []
class Carro:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        

def exibir(item):
    print(item.marca)
    print(item.modelo)
    print(item.ano)
    print(item.cor)

CAMINHO_ARQUIVO = 'C:\\Users\\otavi\\OneDrive\\Documentos\\Programacao-fullstack\\Python\\Orientacao_ a_Objeto\\class_json.json'
def adicionar_banco_de_dados(item):
    banco_dados.append(vars(item))
    with open(CAMINHO_ARQUIVO, 'w',encoding='utf8') as arquivo:
        json.dump(banco_dados,arquivo,ensure_ascii=False,indent=2)

c1 = Carro('FIAT','UNO',2023,'branco')
c2 = Carro('MERCEDES BENS','CLS 300', 2022,'PRETA')
exibir(c1)
adicionar_banco_de_dados(c1)
exibir(c2)
adicionar_banco_de_dados(c2)

class Aviao:
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

with open(CAMINHO_ARQUIVO, 'r',encoding='utf8') as arquivo:
    dados =json.load(arquivo)
    av1 = Aviao(**dados[0])
    av2 = Aviao(**dados[1])
    exibir(av1)
    adicionar_banco_de_dados(av1)
    exibir(av2)
    adicionar_banco_de_dados(av2)