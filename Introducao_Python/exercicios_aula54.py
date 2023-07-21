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


"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_numero_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados :
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(lista, encontra_numero_duplicado(lista))