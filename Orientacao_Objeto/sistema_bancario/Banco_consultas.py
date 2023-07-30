import json
CAMINHO_ARQUIVO = 'C:\\Users\\otavi\\OneDrive\\Documentos\\Programacao-fullstack\\Python\\Orientacao_Objeto\\sistema_bancario\\cadastro.json'

def Consulta_Cpf():
        pesquisa = input('Informe o cpf a Pesquisar: ') # faz a pergunta
        with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
            Banco_dados = json.load(arquivo)
        list(Banco_dados) # transforma em uma lista 
        for item in Banco_dados: #faz a pesquisa no banco de dados
            if pesquisa == item['cpf']:
                resultado = {**item}
                print(resultado)
    

def Consulta_Rg():
    pesquisa = input('Informe o Rg a Pesquisar: ') # faz a pergunta
    with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
        Banco_dados = json.load(arquivo)
    list(Banco_dados) # transforma em uma lista 
    for item in Banco_dados: #faz a pesquisa no banco de dados
        if pesquisa == item['rg']:
            resultado = {**item}
            print(resultado)


def Consulta_Nome():
    pesquisa = input('Informe o Nome a Pesquisar: ') # faz a pergunta
    with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
        Banco_dados = json.load(arquivo)
    list(Banco_dados) # transforma em uma lista 
    for item in Banco_dados: #faz a pesquisa no banco de dados
        if pesquisa == item['nome']:
            resultado = {**item}
            print(resultado)


def Listar_Usuarios_Cadastrados():
    with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo:
        banco =json.load(arquivo)
    list(banco)
    for i in banco:
        print(i)
def Depositar(valor,conta):
    try:
        deposito = float(input('Informe o valor a depositar'))
    except ValueError:
        print('Voce nao informou um valor valido!!')
        Depositar()
    if deposito >= 0:
        resultado = valor
        resultado += deposito
        with open(CAMINHO_ARQUIVO,'r+',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
            Banco_dados = json.load(arquivo)
        list(Banco_dados) # transforma em uma lista 
        for item in Banco_dados: #faz a pesquisa no banco de dados
            if conta == item['conta']:
                item['saldo'] = resultado
        with open(CAMINHO_ARQUIVO,'w+',encoding='utf8') as arquivo:
            json.dump(Banco_dados,arquivo,ensure_ascii=False,indent=1)

def Sacar(valor,conta):
    try:
        saque = float(input('Informe o valor a sacar'))
    except ValueError:
        print('Voce nao informou um valor valido!!')
        Sacar()
    if saque <= valor:
        resultado = valor
        resultado -= saque
        with open(CAMINHO_ARQUIVO,'r+',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
            Banco_dados = json.load(arquivo)
        list(Banco_dados) # transforma em uma lista 
        for item in Banco_dados: #faz a pesquisa no banco de dados
            if conta == item['conta']:
                item['saldo'] = resultado
        with open(CAMINHO_ARQUIVO,'w+',encoding='utf8') as arquivo:
            json.dump(Banco_dados,arquivo,ensure_ascii=False,indent=1)
    else:
        print(f'o valor R${saque} é maior que o saldo R${valor}')

def Consulta_Saldo(conta):
    with open(CAMINHO_ARQUIVO,'r+',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
        Banco_dados = json.load(arquivo)
    list(Banco_dados) # transforma em uma lista 
    for item in Banco_dados: #faz a pesquisa no banco de dados
        if conta == item['conta']:
            print(f"Seu saldo é R$ {item['saldo']}")

def Consulta_Informacoes(conta):
    with open(CAMINHO_ARQUIVO,'r',encoding='utf8') as arquivo: # abre o arquivo e pega as informacoes
        Banco_dados = json.load(arquivo)
    list(Banco_dados) # transforma em uma lista 
    for item in Banco_dados: #faz a pesquisa no banco de dados
        if conta == item['conta']:
            resultado = {**item}
            print(resultado)