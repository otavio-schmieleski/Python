# datetime para utilizar datas
#from datetime import datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
import datetime
from pathlib import Path
from dateutil.relativedelta import relativedelta

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
data1 = datetime(2022,4,10) # no paramentro coloca, o ano, mes e dia
print(data1)

# para pegar data atual
data2 = datetime.now()
print(data2)  

# configurar timezone
data3 = datetime.now(tzinfo = datetime.timezone('Asia/Tokyo')) # pega o time zone de toqui com, o horario atual

# timestamp bom para salvar no banco de dados
print(data2.timestam())
print(datetime.fromtimestamp(1670849077)) # aqui passa os decimais de segundo e converte para data e hora

#from dateutil.relativedelta import relativedelta
relativedelta(year=5) #serve para adicionar mais cinco anos a data e somar datas

#import calendar serve para fazer calendarios
# 0 = segunda e 6= domingo
# locali para interlocalizar a nossa regiao
import locale
locale.setlocale(locale.LC_ALL,'') # para setar tudo da regiao para PT-BR


import calendar
print(calendar.month(2022,12)) # vai printar o mes 12 de 2022
print(calendar.calendar(2023)) # vai pirntar o ano inteiro de 2023
print(calendar.monthrange(2022,12)) # vai printar o ultimo dia e o dia da semana (3,31)
print(list(enumerate(calendar.day_name))) # vai mostras os dia com seus numeros respectivos

# os para trbalahr com o sistema utilizado
import os 
import shutil
Caminho_do_arquivo = 'C:\\Users\\otavi\\OneDrive\\Imagens\\Capturas de tela'
os.system('cls') # serve para limpar o terminar para executar algo no sistema utilizamos os.system('comando')
os.path.join('\\Users','\\otavi','\\OneDrive','\\Imagens','\\Capturas de tela') #serve para passar o caminho do arquivo e contruir um novo
os.walk(Caminho_do_arquivo) # serve para abrir e vereficar todos os diretorios dentro das pastas
os.path.getsize(Caminho_do_arquivo) # retorno o tamanho do arquivo
os.makedirs(Caminho_do_arquivo)

# csv valores separados por virgulas
#import csv
import csv
CAMINHO_CSV = 'C:\\Users\\otavi\\OneDrive\\Documentos\\Programacao-fullstack\\Python\\Orientacao_Objeto\\exemplo.csv'
with open(CAMINHO_CSV,'r',encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    #leitor_lista = csv.DictReader(arquivo) # serve para ler o arquivo como uma lista e podendo manipular ele
    next(leitor)# faz pular a linha do cabecalho

# for i in leitor_lista: aqui pega a coluna apenas de nome
#     print(i['nome'])

# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader() # ESCREVE O CABECHALO DO AQUIVO NO TOPO

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)

# random nao utlizar para gerar senhas e criptografias
import random

# random.randrage(inicio,fim,passo = 1) ou voce escolhe
print(random.randrange(10,20))

# gera um numero aleatorio entre dois interios
print(random.randint(0,10)) # ira sortear numeros de 0 a 10

# gera numeros com ponto flutuantes
print(random.uniform(0,10))# ira sortear numeros de 0 a 10 flutuantes

# secrets serve para fazer uma minir gerador de senha que é mais seguro
import secrets
ramdom = secrets.SystemRandom() # este aqui vai deixar o random mais seguro

# join serve para unir lista
print(''.join(['otavio','marcelo'])) # so para ''.join(e a lista)

#Caminho do arquivo sempre atualiza sozinho
import pathlib
CAMINHO_ARQUIVO = Path(__file__).parent / 'exemplo1.txt' # so coloca o nome do arquivo 
CAMINHO_ARQUIVO_01 = pathlib.Path(__file__).parent / 'exemplo1.txt'

# os.getenv so funciona se declarar a variavel no terminal
import os
senha = os.getenv('Senha')

# nunca enviar o arquivo env para o repositorio
from dotenv import load_dotenv
load_dotenv()
print(os.environ) # serve para mostrar tudo de dicionarios do sistema
#print(os.getenv('BD_PASSWORD')) 

# compactar e descompactar por zip
# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
"""
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)
# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
"""

#executar arquivos com argumentos do sistema
import sys
argumentos = sys.argv

# argparse.ArgumentpARSER PARA ARGUMENTOS MAIS COMPLEXOS
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-b')
args = parser.parse_args()
print(args.b)

if args.b is None:
    print('voce nao passou nenhum argumeto')
else:
    print('voce passou todos os argumentos')


