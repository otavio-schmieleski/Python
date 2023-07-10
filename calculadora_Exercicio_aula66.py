continuar = "sim"
while continuar == "sim" or continuar == True :
    numero = input("informe um numero ")
    numero2 = input("informe um segundo numero ")
    try:
        numero_float = float(numero)
        numero2_float = float(numero2)
    except:
        print("voce nao informou um numero valido")
        continue


    print("1-> + ADICAO  | 2-> - SUBTRACAO  | 3-> * MULTIPLICACAO  | 4-> / DIVISAO") # verefica a opcao escolhida e faz a opracao
    operacao = int(input("qual operacao deseja realizar escolha alguma opcao acima "))
    if operacao == 1 : # faz as operacoes escolhidas
        print(numero_float + numero2_float)
    elif operacao == 2 :
        print(numero_float - numero2_float)
    elif operacao == 3 :
        print(numero_float * numero2_float)
    elif operacao == 4 :
        print(numero_float / numero2_float)
    else :
        print("nao escolheu nenhuma opcao valida")
        continuar = input("deseja continuar [S]sim ou [N]nao ").lower().startswith("s")

    continuar = input("deseja continuar [S]sim ou [N]nao ").lower().startswith("s")