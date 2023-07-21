#comentarios
    # permite escrever comentarios em uma linha

# formatacao do Print
import copy
import sys


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
#global z 
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
    {'nome': 'otavio', 'sobrenome' : 'marcelo'},
    {'nome': 'gabriel', 'sobrenome' : 'vitor'},
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
  
# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))

# dir todos os metodos de uma variavel, hasattr verefica se um metodo esta dentro da variavel
# getattr pega o metodo

# iterables, iterators trabalham com iteraveis

# generator expression ele nao salva na memoria ele espera voce espera o que voce pedir
generator = (n for n in range(100)) # isto é um generator ele salvou na memoria
print(sys.getsizeof(generator)) # este mostra o tamanho em bytes do generator
print(generator)

def generator(n=0):
    yield n # ele pausa a funcao

#try 
try:
    ...
except IndexError: # coloca o  nome do erro para saber qual esta caindo
    ...

try:
    print('ABRIR ARQUIVO')
    8/0
finally: #o finally mais executar mesmo que o try seja executado
    print('FECHAR ARQUIVO')

# raise serve para criar um erro

print(123)
raise ValueError('Deu erro') # ele vai printar este erro na tela

# modulos
#inteiro - import nome_modulo

# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

platform = 'A MINHA'
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

print(platform)

# alias 1 - import nome_modulo as apelido
import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys)


# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex #renomeando o exit
from sys import platform as pf # renomeando a plataform

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

print(platform)
exit()

# modulos
# o primeiro modo que o python acha é o __main__
print('este o modulo', __name__)
#voce pode importar o modulo
import exercicios_aula54 # aqui ele importou o arquivo que eu passei como parametro

from exercicios_aula54 import calculando_numero # importou  do exercico a variavel calculando e posso usar no programa
print(exercicios_aula54.calculando_numero)

# recarregar modulos
import importlib 
importlib.reload(exercicio_aula54) # serve para recarregar o modulo

# importando pack ou pastas os 3 jeitos de importar
from sys import path
import Imc_exercicio_aula29.modulo
from Imc_exercicio_aula29.modulo import altura # importou a variavel altura para está projeto

# nonlocal
# nonlocal valor_final voce pode acessar de dentro de uma funcao e alterar ela
 
# decoradores, sao uma funcao que pode ser criada outra funcao nela e o resultado é gerado uma nova funcao
def fabrica_de_decoradores(a=None, b=None, c=None): # recebe a funcao
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)

# count é um interrador sem fim, esta dentro do metodo (itertools)
from itertools import count # este jeito importa o contador infinito

c1 = count()
for i in c1: 
    if i > 100: # se nao colocar o fim como uma vereficacao ele fica infinito
        break

    print(i)

from itertools import combinations,permutations,product
pessoas = ["joao", "joana","luiz","carlos"]
camisetas = [
    ["preta","branca"],
    ["m","p"]
    ]
def print_iter(iterator):
    print(*list(iterator),sep='\n')

# combinations combina as lista, porem nao repete combina na ordem
print_iter(combinations(pessoas,2))

# permutations combina as lista, porem vem repetido as opcoes combinadas
print_iter(permutations(pessoas,2))

# produt ele concactena as listas e todas elas desempacotando por opcoes, sem repetir
print_iter(product(*camisetas))

# froupby agrupar por valores

# filter vem depois do for 
novos_produtos = [
    p for p in produtos
    if p < 1 # o filtro vem depois do for como aqui estou filtrando tudo que é menor que 1
]
print(novos_produtos)

novos_produtos_1 = filter(
    lambda p:p < 1, pessoa   # aqui faz a mesma coisa que que utilizamos o filter no lugar do if
)


# reduce -- faz a reducao em um valor, tipo o total
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
def funcao_do_reduce(acumulador,produto):
    return acumulador + produto['preco']

total = reduce(
    funcao_do_reduce(), # a funcao
    produtos, # a lista ou dicionario
    0 # inicializa o valor
)

# funcao rercusivas

def recursiva(inicio = 0, fim = 0):
    # caso base
    if inicio >= fim:
        return fim
    # caso recursivo
    #contar até chegar ao fim
    inicio += 1
    return recursiva(inicio,fim)

print(recursiva(5,10))

# venv para criar criar ambiente virtual
# criar uma venv colocamos python -m nome do ambiente
# pip install nome do pacote para instalar
# pip freeze serve para recriar um ambiente virtual ele cria um arquivo txt
# pip freeze > requirements.txt  serve para colocar no git e baixar o mesmo ambiente virtual depois
# quando voce já tem o requirements pode fazer o seguinte codigo:
#pip install -r requirements vai recriar tudo o que estiver neste arquivo com as versoes



# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'aula_de_arquivo.txt'
                                     # e o utf8 codifica para aparecer a acentuacao
arquivo = open(caminho_arquivo, 'w', encoding='utf8') # abre o arquivo com o modo de escrita e apaga tudo que esta no arquivo 
arquivo.close() # fecha o arquivo

arquivo = open(caminho_arquivo, 'a') # abre o arquivo com o modo de escrita e escreve na linha de baixo sem apagar o resto
arquivo.close() # fecha o arquivo

with open(caminho_arquivo, 'w') as arquivo: # o with já abre e fecha o arquivo sozinho e o modo escrita
    print('ola mundo')
    arquivo.seek(0,0) # serve para colocar o curso do arquivo no topo
    arquivo.write('linha 1') # escrevendo no arquivo
    arquivo.writelines( # serve para escrever mais de uma linha por vez
        ('linhas3', 'linha4')
    )

with open(caminho_arquivo, 'r') as arquivo: # abriu e fechou o arquivo lendo
    print(arquivo.read()) # lendo o arquivo
    print(arquivo.readline()) # lendo o arquivo linha por linha
    print(arquivo.readline().strip()) # le o arquivo linha por linha, porem sem os quebra linha

#os.remove(caminho_arquivo) # remove o arquivo

# json tem que importar
# import json
with open('aula_de_Arquivo.json', 'w',encoding='utf-8') as arquivo: # esta inicializando um arquivo json
    json.dump(pessoa,arquivo) # enviando o dicionario para o json

with open('aula_de_Arquivo.json','r', encoding='utf-8') as arquivo: # esta inicializando um arquivo json
    json.load(arquivo) # pegando o json

