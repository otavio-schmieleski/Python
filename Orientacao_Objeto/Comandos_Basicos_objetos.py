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
