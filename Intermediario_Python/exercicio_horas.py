from datetime import datetime
from dateutil.relativedelta import relativedelta
# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

emprestimo = 1_000_000
meses = 60
parcelas = f'R$ {emprestimo / meses:,.2f}'

data_emprestimo = datetime(2020,12,20) # a data passada
delta_anos = relativedelta(year=5) # aumentar a data em 5 anos
data_final = datetime(2025,12,20) # a data final em 60 meses

datas_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final: # um loop para colocar em uma lista
    datas_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

for data in datas_parcelas: # for para printar a lista
    print(data.strftime('%d/%m/%Y'), parcelas)