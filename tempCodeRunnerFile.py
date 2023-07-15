""" adiando execucao da funcao"""
def soma(x,y):
    return x+y
def multiplica(x,y):
    yield x*y
def cria_funcao(funcao,*args):
    return funcao(*args)

soma_com_cinco = cria_funcao(soma,5)
multiplica_por_dez = cria_funcao(multiplica,10)