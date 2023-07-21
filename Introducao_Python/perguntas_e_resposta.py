# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertou = 0
errou = 0
total_pereguntas = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()
    

    for i, opcoes in enumerate(pergunta['Opcoes']):
        print(f"{i})",opcoes)
        i = i + 1

    resposta = pergunta['Resposta']

    resposta_user = input("qual a sua resposta? ")
    total_pereguntas += 1
    if resposta_user == resposta:
        print("VOCE ACERTOU ")
        acertou += 1
    else:
        print("ERROU")
        errou += 1
print(f"Total de acertos: {acertou}")
print(f"Total de erros: {errou}")
print(f"Total de perguntas: {total_pereguntas}")