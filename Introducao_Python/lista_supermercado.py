import os

lista = []
while True:
    lista_enumerada = enumerate(lista)
    print("escolha uma das opcoes")
    usuario = input ("[i]Inserir  [a]Apagar  [l]Listar ").lower() # pede ao usuario a operacao

    if usuario.startswith("i"): # verefica a primeira palavra
        incluir = input("valor: ") 
        os.system("cls")
        lista.append(incluir) # inclui na lista

    elif usuario.startswith("a"): # verefica a primeira palavra
        try:
            excluir = int(input("informe a posicao a apagar: "))
            os.system("cls")
            if excluir in lista :
                lista.pop(excluir) # exclui da lista
                lista_enumerada = enumerate(lista)  # enumera a lista novamente e printa ela
            else:
                print("voce digitou um indice invalido")
        except ValueError: # verefica o erro do usuario digitar uma letra no lugar de numero
            print("digite um valor inteiro")

    elif usuario.startswith("l"): # verefica a primeira palavra e printa a lista completa
        os.system("cls")
        if len(lista) == 0:
            print("nada a listar")
            
        for listar in lista_enumerada:
            print(listar)
    else:
        print("Informe uma opcao valida")