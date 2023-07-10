"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("informe um numero inteiro ")
try:
    numero_int = int(numero)
    calculando_numero = (numero_int % 2)
    if calculando_numero == 0 :
        print(f"o numero digitado {numero} é par")
    else:
        print(f"o numero digitado {numero} é impar")
except:
    print(f"o numero infomado {numero} nao é do tipo inteiro (int)")
    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("informe a hora ")
try:
    hora_float = float(hora)
    if hora_float >= 0 and hora_float <= 11 :
        print(f"bom dia sao exatamente {hora_float}")
    elif hora_float >= 12 and hora_float <= 17 :
        print(f"boa tarde sao exatamente {hora_float}")
    elif hora_float >= 18 and hora_float <= 23 :
        print(f"boa noite sao exatamente{hora_float}")
    else :
        ("nao conheco este horario")
except:
    print(f"numero digitado {hora} nao é um horario")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("informe seu primeiro nome ")
if len(nome) <= 4 :
    print(f"seu nome {nome} é curto")
elif len(nome) == 5 or len(nome) == 6 :
    print(f"seu nome {nome} é normal")
else :
    print(f"seu nome {nome} é muito grande")


"""
exibir os indices da lista
"""
lista = ["mareni","gabriel","otavio","odair"]
i = 0
for nome in lista :
    print(i,nome)
    i += 1

# ou 

indices = range(len(lista)) # gera numeros

for indice in indices:
    print(indice,lista[indice])