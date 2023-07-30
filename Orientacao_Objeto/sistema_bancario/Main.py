from Banco_Login import Autenticar
from Banco_Cadastro import Cadastro,Banco_de_Dados
from Banco_consultas import Consulta_Nome,Consulta_Cpf,Consulta_Rg,Listar_Usuarios_Cadastrados
Start = True

while Start:
    def Usuario():
        print('Deseja fazer:[L]Login  [C]Cadastrar-conta  [F]Consulta-CPF \
[R]Consulta-RG  [N]Consulta-Nome  [U]listar-Usuarios')
        print()
        operacao = input('Informe a Opcao: ')
        if operacao.startswith('L'):
            print('Acessando Banco de Dados...')
            Autenticar()
        elif operacao.startswith('l'):
            print('Acessando Banco de Dados...')
            Autenticar()
        elif operacao.startswith('C'):
            print('Acessando Banco de Dados...')
            Cadastro()
        elif operacao.startswith('c'):
            print('Acessando Banco de Dados...')
            p1 = Cadastro()
            Banco_de_Dados(p1)
        elif operacao.startswith('F'):
            print('Acessando Banco de Dados...')
            Consulta_Cpf()
        elif operacao.startswith('f'):
            print('Acessando Banco de Dados...')
            Consulta_Cpf()
        elif operacao.startswith('R'):
            print('Acessando Banco de Dados...')
            Consulta_Rg()
        elif operacao.startswith('r'):
            print('Acessando Banco de Dados...')
            Consulta_Rg()
        elif operacao.startswith('N'):
            print('Acessando Banco de Dados...')
            Consulta_Nome()
        elif operacao.startswith('n'):
            print('Acessando Banco de Dados...')
            Consulta_Nome()
        elif operacao.startswith('U'):
            print('Acessando Banco de Dados...')
            Listar_Usuarios_Cadastrados()
        elif operacao.startswith('u'):
            print('Acessando Banco de Dados...')
            Listar_Usuarios_Cadastrados()
        else:
            print('Nenhuma Opcao foi selecionada Digite apenas [L]Login ou [C]Cadastrar')
            Usuario()

    Usuario()
    user_question = input('Deseja continuar? [S]sim ou [N]nao ')
    if user_question.startswith('S'):
        Start = True
    elif user_question.startswith('s'):
        Start = True
    elif user_question.startswith('N'):
        Start = False
    elif user_question.startswith('n'):
        Start = False
    else:
        print('Voce escolheu nenhuma opcao!! ')
        Usuario()
    