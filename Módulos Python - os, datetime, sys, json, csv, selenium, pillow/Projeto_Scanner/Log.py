import os
from Autentic_User import Autentic,Banco_de_dados,User_ag,User_name,User_password,banco_valores,name,ag,password
while True:
    os.system('cls')
    print("CONTROLE DE IMOBILIZADOS!")
    opcao = input('Deseja fazer [L]Login ou [C]Cadastrar-se ')
    if opcao.startswith('L') or opcao.startswith('l'):
        Autentic()
    elif opcao.startswith('C') or opcao.startswith('c'):
        p1 = User_name(),User_ag(),User_password()