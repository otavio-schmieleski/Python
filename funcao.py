def multiplicar (*args): # defini uma funcao para receber varios argumentos
    total = 1
    for numero in args: # como é uma tuple estou tirando numero por numero
        total *= numero
    return total 
multiplicacao = multiplicar(1,2,3,4,5) # passando os paramentros para fazer a multiplicacao
print(multiplicacao)

numero = int(input("informe um numero para saber se ele é par ou nao "))
def par_impar(numero):
    if numero % 2 == 0:
        print(f"O numero informado {numero} é par")
    else:
        print(f"O numero informado {numero} é impar")

par_impar(numero)

# funcao que multlipica o numero escolhido e a opcao que o usuario escolher
numero_informado = int(input("Informe um numero "))
print("2-> duplicar  3-> triplicar  4-> quaduplicar")
multiplicador = int(input("informe a opcao escolhida "))

def multi_escolhida(numero_1):
    resultado = 1
    resultado *= (numero_informado * multiplicador)
    return resultado

print(f"o numero {numero_informado} foi multiplicado por {multiplicador} = {multi_escolhida(numero_informado)}")