nome = input("informe seu nome \n")
sobrenome = input("informe seu sobrenome \n")
idade = int(input("informe sua idade \n"))
ano_nascimento = 2023 - idade
maior_de_idade = idade >= 18
altura_metros = input("informe sua altura em metros \n")

print("\n\n\n")

print("Nome:", nome)
print("Sobrenome: ", sobrenome)
print("Idade: ", idade)
print("Ano de Nascimento: ", ano_nascimento)
print("É maior de idade ? ", maior_de_idade)
print("Altura em metros: ", altura_metros)