import sqlite3
from pathlib import Path
ROOT_DIR = Path(__file__).parent

DB_FILE = ROOT_DIR / 'db.sqlite3'
TABLE_NAME = 'customers'

conection = sqlite3.connect(DB_FILE) # serve para copnectar no banco de dados
cursor = conection.cursor()

#SQL
# CRUD - CREATE READ   UPDATE DELETE
# SQL -  INSERT SELECT UPDATE DELETE

# criar a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}' # SERVE PARA CRIAR UMA TABELA
    '(id INTEGER PRIMARY KEY AUTOINCREMENT,' # CHAVE PRIMARIA DA TABELA E ENCREMENTA O ID NA TABELA 1,2,3
    'name TEXT,'
    'weight REAL'
    ')'
)
conection.commit() # salvando a tabela 

# Registrar valores na colunas da tabela

# insere apenas uma valor por vez na base de dados
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id,name,weight)'
    'VALUES (NULL, "OTAVIO", 9.8)'
)
conection.commit()
# insere mais de um valor por vez na base de dados
#cursor.executemany()

# CRIA UM FILTRO
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

# PRINTA A TABELA INTEIRA PELO FETCHALL 
for row in cursor.fetchall():
    _id,name,weight = row
    print(_id,name,weight)

# DELETA TODA  A TABELA SE NAO PASSAR O WHERE
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

# DELETE COM WHERE TEM QUE PASSAR UM PARAMETRO como o name e o nome do arquivo sqlite
# cursor.execute(
#     f' DELETE FORM sqlite_sequence WHERE name ="{TABLE_NAME}"' 
#       ou
#     f'WHERW id = 1'
# )

# UPDATE COM WHERE ele vai alterar o id
cursor.execute(
    f'UPDATE {TABLE_NAME} SET name="Qualquer" WHERE id=2 '
)
conection.commit()

cursor.close() # fechou o cursor
conection.close() # fechou a conecao com o arquivo
