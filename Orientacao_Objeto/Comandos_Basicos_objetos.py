from datetime import datetime
from pytz import timezone
# criando class
# uma classe pode gerar varias instancias
# na class o self é a mesma da class
class Pessoa:
    def __init__(self,nome,sobrenome): # metodos sempre vai receber o self referencia a class, do lado as propiedades
        self.nome = nome # o self é a class e declaramos como nome e depois passamos as propiedades
        self.sobreno = sobrenome
p1 = Pessoa('otavio','marcelo')# criando novo objeto
print(p1.nome)# vai printar o nome 

class Carro:
    def __init__(self,nome,marca): # aqui pedimos o argumentos
        self.nome = nome #  self sempre vai estar aqui 
        self.marca = marca
fusca = Carro('fusca','wolkvagens') # passamos os argumetos po#s ped#mos na #n#c#al#zacao

# para criar atributo dentro da class
class Pessoas:
    ano_atual = 2023 # isto é um atributo extremamente da class
    def __init__(self,nome,idade):
        self.nome='nome'
    def get_ano_nascimentos(self):
        return Pessoas.ano_atual - self.idade

p2 = Pessoas('otavio',18)
print(p2.nome,p2.get_ano_nascimentos())

# @staticmethod nao tem acesso ao self dentro da class
# @classmethod podemos receber da prorpia class
class Carro:
    def __init__(self,nome,marca): # aqui pedimos o argumentos
        self.nome = nome #  self sempre vai estar aqui 
        self.marca = marca

    @classmethod
    def create_auth(cls,user,password): # aqui so pegamos a class o cls e usamos em baixo sem init 
        carro = cls()
        carro.user = user
        carro.password = password
        return carro

    @staticmethod # nao recebe o self
    def soma(x,y):
        return x+y

    def get_cor(self): # deste jeito voce utiliza o get para nao mexer na variavel nome
        return self.nome
    
    @property # funciona igual um get como um metodo
    def cor(self):
        return self.nome 

class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor
        self._cor = self.cor # atributo que comeca com _ nao deve ser usado fora da class
        self._cor_tampa = None
    @property # aqui é o get igual para pegar e o usuario usar
    def cor(self):
        return self._cor
    
    @cor.setter # como defenimos o setter no python
    def cor(Self,valor):
        Self._cor = valor # aqui mudamos o valor

    @property # aqui é um exemplo do getter e setter logo em baixo da tampa da caneta0
    def cor_tampa(self):
        return self._cor_tampa
    @cor_tampa.setter
    def cor_tampa(Self,valor):
        Self._cor_tampa = valor

"""
(sem underline) é publico
self.public 
(com 1 underline) é protectec
self._protected
(com 2 underline) é private
self.__private
"""
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())


class Pessoa: # aqui fazemos a class mae a mestre de todas as outras
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Cliente(Pessoa): # aqui eu usei a class pessoa passando no parentese a class que dejeso buscar 
    ...

print(Cliente('otavio','marcelo')) # aqui ele ja pediu as informacoes da class pessoa em cliente

#super() é sobre chamar a class mae para alterar o metodo 
# abstratc import abstract 
# a abstracao nao deve ser utilizada
#@abstractmethod serve para fazer algo abstrato
# from abC import ABC, abstractmethod para importar a abstracao
# polimorfismo
from abc import ABC, abstractmethod # IMPORTANDO METODO ABSTRATO

class Notificacao(ABC): # aqui chama o metodo da abstracao tipo a biblioteca
    def __init__(self,mensagem):
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self): # aqui o metodo enviar nao pode ser acessado por aqui, mas sim em outra class
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self): 
        print('email:enviando',self.mensagem)

class NotificacaoSms(Notificacao):
    def enviar(self): 
        print('SMS:enviando',self.mensagem)

NotificacaoSms('bom dia')
NotificacaoEmail('oi')

# para lancar uma execao colocamos tipo
class MeuError(Exception): # aqui para fazermos algum erro para o usuario
    ...
class Erro(MeuError):
    Exception.add_note('mais um erro') # paraa adicionar outra nota de erro no terminal
    raise MeuError('erro') # aqui ele manda para o terminar a mensagem de erro
Erro()

# __dunder__ metodos, cuidar os parametros que deve ser passados
# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y): # serve para inicializar a class
        self.x = x
        self.y = y

    def __repr__(self): # serve para sabermos qual é o tipo de dado de determinado atributo e exibilo na tela
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})' #colocamos o !r para ele passar as string com '-'

    def __add__(self, other): # o__add__ faz junção de dois atributos
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other): #__gt__ faz a comparaccao entre ds atributos e retorna boolean
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

    def __enter__(self): # serve para iniciar algo que tenha que entra ou conectar e depoism precise fechar com o exit
        print('abrindo um arquivo')
    def __exit__(self): #  fecha o __enter__ 
        print('fechando o arquivo')


if __name__ == '__main__': 
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)


# funcoes decoradoras

def meu_repr(self): # faz a funcao rper
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr # chama a funcao repr
    return cls


@adiciona_repr # aqui adiciona o repr aqui decora o metodo
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome): # aqui voce coloca o __Call__ para fazer ser igual a um executavel
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('23945876545')
call1('Luiz Otávio') # e pode ser chamado deste jeito agora

# class decoradora

# namedtuples tuplas imutaveis
from collections import namedtuple

Carta = namedtuple('carro',['valor','naipe'])# no valor podemos colocar outra coisa
as_espadas = Carta('a','espada')# assim configura uma namedtuple com dados
print(as_espadas)

# para executar apenas no arquivo
if __name__ == 'main':
    print('executando apenas neste bloco sem executrar em outro modulo')





