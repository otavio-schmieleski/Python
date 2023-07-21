# copy, sorted, produtos.sort
# Exercícios
import copy


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

lista_preco_alterado=[]
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = []
novos_produtos= copy.deepcopy(produtos)
# Aumente os preços dos produtos a seguir em 10%
for preco in produtos:
    lista_preco_alterado.append(f"{preco['preco'] * 1.1:.2f}")

for i,item in enumerate(novos_produtos): # adicionando a lista com o preco já alterado
    item['preco'] = lista_preco_alterado[i] 

print(*novos_produtos, sep='\n')
print()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_oredenados_por_nome = copy.deepcopy(novos_produtos)
# Ordene os produtos por nome decrescente (do maior para menor)
def ordena_nome(ordenador):
    return ordenador['nome']
produtos_oredenados_por_nome.sort(key=ordena_nome,reverse=True)

print(*produtos_oredenados_por_nome, sep='\n')
print()

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted( # criou o sorteador e utilizou lambda 
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)
# Ordene os produtos por preco crescente (do menor para maior)


print(*produtos_ordenados_por_preco, sep='\n')

""" adiando execucao da funcao"""
def soma(x,y):
    return x+y
def multiplica(x,y):
    return x*y
def cria_funcao(funcao,*args):
    def interna(y): 
        return funcao(*args)

soma_com_cinco = cria_funcao(soma,5)
multiplica_por_dez = cria_funcao(multiplica,10) 




"""
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

"""
Estado = ['Salvador', 'Ubatuba', 'Belo Horizonte']
Estado_slim = ['BA', 'SP', 'MG', 'RJ']
Estados_completos = []
def zipper():
    for i,estados in enumerate(Estado):
        juncao = estados,Estado_slim[i]
        Estados_completos.append(juncao)
zipper()
print(Estados_completos)

print(list(zip(Estado,Estado_slim))) # o zip une lista a mesma coisa da funcao de cima



lista_1 = [1,2,3,4,5,6,7]
lista_2 = [1,2,3,4]

def tamanho_da_lista(l1,l2):
    global lista_maior
    if len(l1) < len(l2):
        lista_menor = lista_1
        lista_maior = lista_2
    else:
        lista_menor = lista_2
        lista_maior = lista_1
    return lista_menor

resultado_lista_menor = tamanho_da_lista(lista_1,lista_2)
lista_soma=[]
def soma():
    for i,numeros in enumerate(resultado_lista_menor):
        soma_lista = numeros + lista_maior[i]
        lista_soma.append(soma_lista)

soma()
print(lista_soma)

#ou 
# esta é a maneira de se fazer em python mais simples
lista_soma2 = [
    x + y for x, y in zip(lista_1, lista_2)
]
print(lista_soma2)