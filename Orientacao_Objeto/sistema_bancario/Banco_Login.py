import json
CAMINHO_ARQUIVO = 'C:\\Users\\otavi\\OneDrive\\Documentos\\Programacao-fullstack\\Python\\Orientacao_Objeto\\sistema_bancario\\cadastro.json'
from Banco_consultas import *
from Banco_Cadastro import Cadastro,Banco_de_Dados

def Autenticar():
    global conta
    conta = input('Informe sua conta ')
    with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
        Banco_dados = json.load(arquivo)
    list(Banco_dados) # transforma em uma lista 
    for item in Banco_dados: #faz a pesquisa no banco de dados
        if conta == item['conta']:
            resultado = {**item}
            Opcoes = input('Deseja [S]sacar | [D]depositar  | [C]consulta Saldo  | [I]informacoes Pessoais ')
            if Opcoes.startswith("s"):
                Sacar(item["saldo"],conta)
            elif Opcoes.startswith('s'):
                Sacar(item["saldo"],conta)
            elif Opcoes.startswith('D'):
                Depositar(item["saldo"],conta)
            elif Opcoes.startswith('d'):
                Depositar(item["saldo"],conta)
            elif Opcoes.startswith('C'):
                Consulta_Saldo(conta)
            elif Opcoes.startswith('c'):
                Consulta_Saldo(conta)
            elif Opcoes.startswith('I'):
                Consulta_Informacoes(conta)
            elif Opcoes.startswith('i'):
                Consulta_Informacoes(conta)
            else:
                print('Nenhuma opcao foi selecionada')
                Autenticar()
        else:
            continue
    user_question = input('Deseja fazer [L]Login ou [C]Cadastrar conta ou [S]sair')
    if user_question.startswith('L') :
        print('Acessando Banco de Dados...')
        Autenticar()
    elif user_question.startswith('l'):
        print('Acessando Banco de Dados...')
        Autenticar()
    elif user_question.startswith('C'):
        print('Acessando Banco de Dados...')
        p1 =Cadastro()
        Banco_de_Dados(p1)
    elif user_question.startswith('c'):
        print('Acessando Banco de Dados...')
        p1 =Cadastro()
        Banco_de_Dados(p1)
    elif user_question.startswith('S'):
        print('Saindo do Sistema!!')
    elif user_question.startswith('s'):
        print('Saindo do Sistema!!')