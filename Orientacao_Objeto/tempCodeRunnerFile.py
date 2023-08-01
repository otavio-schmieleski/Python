import csv
CAMINHO_CSV = 'C:\\Users\\otavi\\OneDrive\\Documentos\\Programacao-fullstack\\Python\\Orientacao_Objeto\\exemplo.csv'
with open(CAMINHO_CSV,'r',encoding='utf-8') as arquivo:
    #leitor = csv.reader(arquivo)
    leitor_lista = csv.DictReader(arquivo) # serve para ler o arquivo como uma lista e podendo manipular ele
    #next(leitor)# faz pular a linha do cabecalho

for i in leitor_lista:
    print(i['nome'])