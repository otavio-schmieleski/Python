from collections import namedtuple

Carta = namedtuple('carro',['valor','naipe'])
as_espadas = Carta('a','espada')
print(as_espadas)