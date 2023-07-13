#comentarios
    # permite escrever comentarios em uma linha

# formatacao do Print
import copy


print("mostra algo na tela") #String em aspas duplas ou simples
print(12,10)
print(22,4,2022, sep="/")# SEP significa o separador entre o 22, 04 e 2005
print(12,10, sep="-", end="\n") # END significa para modificar o final do print
print(12 + 10)

# Tipos de dados
print(12) # numero inteiro
print(1.1) # numero float
print(type(1.1)) # para saber qual o tipo do argumento utilizado 
print(10 == 10) # Sim => True(Verdadeiro)
print(10 == 11) # Nao => False(Falso)

# conversao de Variaveis
print(int("1")) # serve para converte uma string em interio
print(str(10)) # serve para converter inteiro em string
print(bool(" ")) # serve para converter string em boolean V ou F

# Variaveis
nome_completo = "otavio schmieleski costa" # declarando uma variavel string
soma = 10 + 10 # declarando uma variavel int ou float
idade = 18
sexo_masculino = True # declarando uma variavel boolean
maior_De_idade = idade >= 18
print(nome_completo,soma,maior_De_idade, sep=" - ")


# Operadores logicos
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)


# concatnacao
print("otavio" + " " + "marcelo")


# prioridade de execucao
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + - 
cont_1 = 1 + 1 ** 5 + 5 
print(cont_1)


# formatacao de string e int
print(f"{cont_1} tem {modulo} de {exponenciacao}") # coloca o f na frente e as {} para colocar a variavel nop texto
print(f"{exponenciacao:.2f}") # serve para colocar duas casas decimais no numeros
formato = "a={}, b={}, c={}".format("a","b","c") # para conctatenar com index
formato = "a={1}, b={2}, c={0}".format("a","b","c") # podendo colocar a ordem dos elementos escolhidos
print(formato)


# Input
nome = input("Qual o seu nome? ") # pede algo para o usuario digitar
print(nome)


# if e elif e else
entrada = input('voce quer "entra" ou "sair?" ')
if entrada == "entrar" :
    print("voce acessou o sistema")
elif entrada == "sair" :
    print("voce nao acessou o sistema")
else :
    print("voce nao digitou nada de entrar ou sair")


# Operadores aritimericos
"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""


    # operadores logicos
# and todas as condicoes precisam ser verdadeiras para ser true, senao é falso
entrada = input("[E] entrar [S] sair ")
senha_digitada = input("senha ")
senha_permitida = "123456"
if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("sair")


# or quando há uma condicao verdadeira tudo é vira verdadeiro
entrada = input("[E] entrar [S] sair ")
senha_digitada = input("senha ") or "sem senha"
senha_permitida = "123456"
if (entrada == "E" or entrada == "e" )and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("sair")


# not inverter as expressoes, != se é verdadeira vira falsa
senha = input("senha: ")
if senha != senha_permitida:
    print("logado com sucesso")


# in verefica se tem algo dentro da variavel
nome = "otavio marcelo"
if " " in nome : # se na variavel nome tiver espaco ele vai printar 
    print("seu nome tem espaco")


# string interaveis
nome = "otavio"
print(nome[0])
print(nome[4])


# Interpolacao de strings 
"""
s - string 
d e i - int
f - float
x e x - hexadecimal

coloca o porcentagem na frente e despois o que se refere a varialvel string, int, float etc
"""
nome = "otavio"
preco = 10
interpolacao = "%s, o preco é R$%.2f" % (nome,preco)#uma variavel string %S e uma variavel float %f e no lado coloca as variaveis
print(interpolacao)


# formatacao de string
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
.lower()  serve para colocar as palavras em minicuslo
.startswith("s") serve para pegar a primeira palavra digitada
.count("palavra") serve para contar quantas vezes a palavra apareceu na frase
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f"o hexadecimal de 1500 é {1500:08X}")

# fatiamento de string
letras = "ola mundo"
print(letras[4:]) # pega a fatia das letras, da posicao 4 ate o final
print(len(letras)) # serve para contar o tamnaho da variavel len
print(letras[::-1]) # serve para fazer a variavel invertida


# try -> tentar executar o codigo
# except -> ocooreu algum erro ao tentar executar
numero = input("vou dobrar o numero digitado")
if numero.isdigit(): # verefica se o ussuario digitou apenas numeros
    numero_float = float(numero) 
    print(f"o dobro de {numero} é {numero_float * 2:.2f}") # o if nao evita as essecoes diferente do try/except
else:
    print("nao é um numero")

# a diferenca é que se o bloco do try der errado ele pula para o except, ele nao quebra o codigo
try:
    numero_float = float(numero)
    print(f"o dobro de {numero} é {numero_float * 2:.2f}") # o if nao evita as essecoes diferente do try/except
except:
     print("nao é um numero")


# CONSTANTE = "variaveis que nao  muda"
# no python nao existe constante mais para dizermos se é constante colocamos a variavel em MAISCULA
NOME_NAO_MUDA = "otavio"


# identidades de variaveis
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')


# while execute uma acao enquanto uma condicao for verdadeira
condicao_01 = True

while condicao_01:
    nome = input("qual o seu nome: ")
    print(f"seu nome é {nome}")
    break # serve para encerrar o loop parar ele

contador = 0
nome_novo = "*"
nome = input("informe seu nome: ")
while contador < len(nome):
    nome_novo += f"{nome[contador]}*"
    contador = contador + 1
print(nome_novo)


# for execute ate que seja possivel executar até ser setado
# range -> range(start,stop,step)
# next -> entrega o proximo valor
# iter -> entrega o seu iterador

texto = "python"
for letra in texto : # ele vai salvar na variavel letras todas as palavras do texto
    print(letra) 

numeros = range(10) # numeros ate 10
numeros = range(0,10) # numeros de 0 a 10 
numeros = range(0,10,2) # numeros de 0 a 10 pulando de 2 em 2

for numero in numeros : # for *** in variavel, no *** coloca o nome de uma nova variavel que vair ser armazenada a variavel vereficada
    print(numero)

lista = ["otavio","gabriel"]
for nome in lista: # roda toda a lista
    print(nome)


# list [] suporta qualquer valor
# metodos uteis:
# type() serve para falar o tipo da variavel na lista
"""Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [123,"String",True,1.21]

# del lista[posicao] serve para deletar o elemento da lista
del lista[0]

# append(valor) adiciona um valor no final da lista
lista.append(10)

# pop() remove o ultimo elemento da lista atual ou passa o index no ()
lista.pop()

# del deleta o elemto da lista
del lista[1]

# clear limpa a lista
lista.clear()

# insert serve para inserir uma variavel a lista ao index escolhido (posicao,valor)
lista.insert(0,5)

# + - concatena a lista
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a - lista_b

# extend (nome da lista a extender) para extender a lista
lista_a.extend(lista_b)

# copy() serve para copiar uma listya ou algo 
lista_a = ["otavio","amanda"]
lista_b = lista_a.copy()

#desempacotamento o *resto para nao dar erro
nome1,nome2,nome3,*resto = ["otavio","gabriel","odair","mareni"] # cada nome representa um nome
print(nome3)

# tupla -> uma lista imutavel
tupla = ("otavio","joao","costa") # isto é uma tupla que nao pode ser mudada
tupla = tuple(lista_a) # converte a lista para tupla
lista_o = list(tupla) # converte uma tupla para lista podendo assim editala

# enumerate -> enumera iteraveis
lista_r = ["otavio","costa"]
lista_enumerada = enumerate(lista_r) # enumerando a lista
for item in lista_enumerada: # printando a lista completa  
    print(item)

# round() serve para aredondar as casas decimais
numero_1 = 0.1
numero_2 = 0.8
print(round(numero_1+numero_2, 2)) # vai aredondar em duas casas decimais

# slip divide as string
frase = "ola so que, coisa interessante"
lista_frases = frase.split() # vai separa nos espacos em brancos
print(lista_frases)
lista_virgula = frase.slip(",") # vai separa nas virgulas
print(lista_virgula)

# strip cortar os espaco e join une as string

# lista dentro de lista
salas = [
        #0       1
    ["otavio","maria"], # 0

        #0
    ["jose"], # 1

        #0      1       2
    ["odair","mareni","joao"], # 2

        #0       1       2         3
    ["odair","mareni","joao", (10,20,30)], # 3
]
# para acessar um indice coloca o indece e a posicao
print(salas[2][1]) # ele vai pegar o indice 2 que é a lista ["odair","mareni","joao"], # 2 e o indice mareni
print(salas[3][3][2]) # ele vai peghar o indeci de dentro da tupla e retorno o 30

"""
Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)

The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""
# replace 
#.replace("o que voce quer subistituir","aqui coloque pelo oque")



"""--------------------------------------------comandos intermediarios-------------------------------------------------------------------"""

# def -> funcao serve para estrutura o codigo, depois voce pode chama - la no codigo
def funcao():
    print("ola")
    print("bom dia")

# e tambem podemos colocar uma variavel para que seja passada
def saudacao(nome):
    print(f"seu nome é{nome}")

saudacao("otavio")

# definicao da funcao que tem 2 parametros
def soma (x,y):
    print(x+y)

#execucao
soma(1,2)
soma(y=2,x=1)# neste caso usamos o argumentos com parametros invertidos eles estando nomeados

# is not nao é
if z is not None:
    print("x nao é vazio, nao esta vazio")

# escopo global pode alcancar qualquer variavel 
global z 
# escopo local pode acessa apenas no escopo da funcao

# return retorna um valor

def multi (n,m):
    return(n*m)

retorna = multi(1,2) # podemos colocar o resultado em uma variavel
print(retorna)

#*args sao argumentos que podemos colocar varios argumentos na funcao
def arg(*args):
    print(arg)
arg(1,2,3,4,5,6)

# sum serve para somar
print(sum(1,2))

# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

# del exclui 

# Métodos úteis dos dicionários em Python
# len - quantas chaves
print(len(pessoa))
# keys - iterável com as chaves
print(pessoa.keys())
# values - iterável com os valores
print(pessoa.values())
# items - iterável com chaves e valores
print(pessoa.items())
# setdefault - adiciona valor se a chave não existe
print(pessoa.setdefault("idade",0))
# copy - retorna uma cópia rasa (shallow copy)
print(pessoa.copy())
print(copy.deecopy(pessoa))
# get - obtém uma chave
print(pessoa.get("nome"))
# pop - Apaga um item com a chave especificada (del)
print(pessoa.pop("nome"))
# popitem - Apaga o último item adicionado
print(pessoa.popitem())
# update - Atualiza um dicionário com outro
print(pessoa.update({"sexo": "masculino",})) # aqui ele vai adicionar o sexo ao dicionario pessoa

# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.
# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)
# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)


# lista.sort() ordena a lista
lista_frases.sort()

# lista.sort(reverse=True) ordena a lista ao contrario
lista_frases.sort(reverse=True)

# lista.sorte(Key= nome da funcao)# serve para voce informar como quer que a lista seja ordenada
lista = [
    {'nome': 'otavio', 'sobrenome' : 'marcelo'}
    {'nome': 'gabriel', 'sobrenome' : 'vitor'}
    {'nome': 'odair', 'sobrenome' : 'costa'}
]
def ordena(item):
    return item['nome']

lista.sort(key=ordena) # neste sorte ele vai ordenar por nome

#lambda
def executa(funcao,*args):
    return funcao(*args)

print(
    executa(
        lambda x,y: x+y # lambda nao usa nome é passa tudo sem parentese e o return é na mesma linha
    )
)

# para extrair uma lista em outra lista usamos **
pessoa_completa = {**lista,**lista_a} # pegamos a lista e a lista_a e colocamo em outra lista

# **kwargs serve para dar elementos nomeados variaveis tipo args
def nome (*args,**kwargs): # aque podemos colocar varios elemneots nomeados para a funcao
    ...

# comprehension é forma rapida de criar lista
lista_numero = [numero for numero in range(10)] # ele vai adicionar 10 numeros a lista, mas temos que passar o variavel na esquerda para criar a lista

# filtrar listar
        #n mapeamento             filtro  
lista_2 = [n for  n in range(10) if n < 5] # o filtro em depois do for neste caso o if
  
