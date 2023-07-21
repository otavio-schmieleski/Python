class Pessoas:
    ano_atual = 2023 # isto é um atributo extremamente da class
    def __init__(self,nome,idade):
        self.nome='nome'
    def get_ano_nascimentos(self):
        return Pessoas.ano_atual - self.idade

p2 = Pessoas('otavio',18)
print(p2.nome,p2.get_ano_nascimentos())