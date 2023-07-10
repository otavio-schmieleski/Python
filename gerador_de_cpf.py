"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""   

import os
import random
continua = "sim"

while (continua.startswith("s")):
    opcoes = input("Desejar [G] gerar um CPF  ou [V] validar seu CPF ")
    if opcoes.startswith("G",) or opcoes.startswith("g"):
        cpf = []
        cpf_calculado = []
        cpf_digitado = []
        for i in range(9) :
            cpf_digitado.append(random.randint(0, 9))
        # se o usuario digitou 11 ele passa paar a proxima etapa
        multiplica = 10
        resultado = 0
        indice = 0

        # faz a conta do primeiro numero do cpf
        for lista in cpf_digitado[:9]:
            cpf.append(int(lista))
            resultado += (cpf[indice]* multiplica)
            indice += 1
            multiplica -= 1
        primeiro_digito = (resultado * 10) % 11

        if primeiro_digito > 9 :
            cpf.append(0)
        else:
            cpf.append(primeiro_digito)
        
        # faz a conta do segundo numero do cpf
        multiplica_2 = 11
        resultado_2 = 0
        indice_2 = 0
        for lista_2 in cpf_digitado[:9] :
            resultado_2 += (cpf[indice]* multiplica_2)
            indice_2 += 1
            multiplica_2 -= 1
        segundo_digito = (resultado_2 * 10) % 11

        if segundo_digito > 9 :
            cpf.append(0)
        else:
            cpf.append(segundo_digito)

        print(f"este é seu CPF:{cpf}")

    elif opcoes.startswith("V") or opcoes.startswith("v"): 
        cpf = []
        cpf_calculado = []
        cpf_digitado = input("digite os primeiros 9 digitos do seu cpf ").replace(".","").replace(" ","").replace("-","")
        entrada_valida = cpf_digitado[0] * len(cpf_digitado)
        # se o usuario digitou 11 ele passa paar a proxima etapa
        if len(cpf_digitado) == 11 and entrada_valida != cpf_digitado:
            multiplica = 10
            resultado = 0
            indice = 0

            # faz a conta do primeiro numero do cpf
            for lista in cpf_digitado[:9]:
                cpf.append(int(lista))
                resultado += (cpf[indice]* multiplica)
                indice += 1
                multiplica -= 1
            primeiro_digito = (resultado * 10) % 11

            if primeiro_digito > 9 :
                cpf.append(0)
            else:
                cpf.append(primeiro_digito)
            
            # faz a conta do segundo numero do cpf
            multiplica_2 = 11
            resultado_2 = 0
            indice_2 = 0
            for lista_2 in cpf_digitado[:9] :
                resultado_2 += (cpf[indice]* multiplica_2)
                indice_2 += 1
                multiplica_2 -= 1
            segundo_digito = (resultado_2 * 10) % 11

            if segundo_digito > 9 :
                cpf.append(0)
            else:
                cpf.append(segundo_digito)

            # transforma o que o usuario digitou em uma lista do tipo inteira para fazer a vereficacao
            for inteiro in cpf_digitado:
                cpf_calculado.append(int(inteiro))

            # verefica se o cpf digitado pelo usuario é valido
            if cpf == cpf_calculado :
                print(f"{int(cpf_digitado)} é valido")
            else:
                print("CPF invalido")
            continua = input("deseja gerar outro CPF [S] sim  |  [N]nao ")
        else :
            print("digite apenas 11 digitos e nao sequenciais")