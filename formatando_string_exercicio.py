nome = input("informe seu nome ")
idade = input("informe sua idade ")
if nome != "" and idade != "" :
    print(f"seu nome é {nome}")
    print(f"seu nome invertido é {nome[::-1]}")
    if " " in nome :
        print("seu nome contem espacos")
    else:
        print("seu nome nao contem espaco")
    print(f"seu nome contém {len(nome)} letras")
    print(f"a primeira letra do seu nome é {nome[0]}")
    print(f"a ultima letra do seu nome é {nome[len(nome) -1 ]}")
else :
    print("desculpe, voce deixou campos vazios")