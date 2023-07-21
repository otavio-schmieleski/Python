import os
import random

palavra_secreta = ["python","java","nodejs","css","javascript","pycharm","c","html","typscript","jango"]
sorteador = random.randrange(0,9,1)
letras_acertadas = ""
tentativas = 0
acertos = 0
erros = 0
while True :
    letra_digitada = input("Digite  uma letra: ")

    if len(letra_digitada) > 1:
        print("digite apenas uma letra")
        tentativas += 1
        continue
    
    if letra_digitada in palavra_secreta[sorteador]: # se a palavra digitada estiver dentro da palavra secreta
        letras_acertadas += letra_digitada
        acertos += 1
    else:
        erros += 1
    
    palavra_formada = ""
    for letra_secreta in palavra_secreta[sorteador] : # pega cada palavra da pálavra_secreta e traz para a letra_secreta
        if letra_secreta in letras_acertadas: # compara se a letra pegada ja foi acertado e printa se nao coloca *
            palavra_formada += letra_secreta
        else :
            palavra_formada += "*"

    print(palavra_formada)
    tentativas += 1
    if palavra_formada == palavra_secreta[sorteador]:
        os.system('cls')
        print("voce ganhou!!")
        print(f"a palavra secreta era {palavra_secreta[sorteador]}")
        print(f"o total de acertos foi de : {acertos}")
        print(f"o total de acertos foi de : {acertos}")
        print(f"o total de tentativas foi de : {tentativas}")
        break