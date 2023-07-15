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