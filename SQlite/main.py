import pymysql
import os
import dotenv
dotenv.load_dotenv()
# configuracoes padroes apenas muda os nomes dependendo do servidor
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)
TABLE_NAME = 'customers'

with connection:
    with connection.cursor() as cursor:
        #SQL
        # limpa a tabela
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

        #criacao de tabela com colunas id, nome, idade
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL , '
            'PRIMARY KEY (id)'
            ')'
        )
        # INSERE ALGO NA PLANILHA NO LUGAR DO NOME E IDADE
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES ("OTAVIO", 18) '
        )
        # aqui serve para enserir no banco de dados porem passa os dados depois quando executar
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome,idade) VALUES (%s,%s) '
        )
        # aqui passa os valores para o banco de dados, chamando o metodo acima
        cursor.execute(sql, ('MARCELO', 17))
        # ou assim também 
        dados = ('COSTA',19)
        cursor.execute(sql,dados)

        # dicionario data2
        data2 = {
            'nome':'le',
            'idade': 27,
        }
        # aqui vai pega os valores do dicionario 
        sql_varios_itens = (
            f'INSERT INTO {TABLE_NAME} '
            #tem que colocar entre () e passar as chaves dos dicionarios
            '(nome,idade) VALUES (%(nome)s,%(idade)s) '
        )
        cursor.execute(sql_varios_itens,data2)

        # interavel de tupla e dicionario
        data3 = (
            {'nome':'Lhe','idade': 87,},
            {'nome':'She','idade': 68,},
            {'nome':'CHE','idade': 54,},
            {'nome':'LUX','idade': 26,},
            {'nome':'PYT','idade': 82,},
        )
        
        #aqui pega o valor do interavel
        sql_iteravel = (
            f'INSERT INTO {TABLE_NAME} '
            #tem que colocar entre () e passar as chaves dos dicionarios
            '(nome,idade) VALUES (%(nome)s,%(idade)s) '
        )
        #tem que ser executemany para passar um interavel para ele executar
        cursor.executemany(sql_iteravel,data3)

        # interavel de tupla 
        data4 = (
            ('OTA', 12),
            ('VIO', 8,),
        )
        
        #aqui pega o valor do interavel
        sql_iteravel_tupla = (
            f'INSERT INTO {TABLE_NAME} '
            #tem que colocar entre () e passar as chaves dos dicionarios
            #os valores na tupla devem ser passado na ordem correta
            '(nome,idade) VALUES (%s,%s) '
        )
        #tem que ser executemany para passar um interavel para ele executar
        cursor.executemany(sql_iteravel_tupla,data4)

    #Lendo os valores com SELECT
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id = 3 ' # aqui vai pega apenas o 3 valor
            
        )
        # aqui passa os valores para o banco de dados, chamando o metodo acima
        cursor.execute(sql) 

        data5 = cursor.fetchall() # serve para selecionar tudo da base de dados
        # aqui vai mostrar tudo da¿o banco de dados
        for row in data5:
            print(row)
        

    #DELENTANDO VALORES DO BANCO DE DADOS COM DELETE
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} ' # DELETE SEM WHERE PAGA TUDO DO BANCO DE DADOS
            'WHERE id = 4 ' # aqui ele so vai deletar o id 4 do banco de dados
        )
        # aqui passa os valores para o banco de dados, chamando o metodo acima
        cursor.execute(sql) 

        data6= cursor.fetchall() # serve para selecionar tudo da base de dados
        # aqui vai mostrar tudo da¿o banco de dados
        for row in data5:
            print(row)
    
    #UPDATE VALORES NO BANCO DE DADOS
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE FROM {TABLE_NAME} ' # UPDATE SEM WHERE MODIFICA TUDO DO BANCO DE DADOS
            'SET nome=%s, idade=%s '
            'WHERE id = 2 ' # aqui ele so vai MODIFICAR o id 4 do banco de dados
        )
        # aqui passa os valores para o banco de dados, chamando o metodo acima
        cursor.execute(sql,('eleonor',102))

        data7 = cursor.fetchall() # serve para selecionar tudo da base de dados
        # aqui vai mostrar tudo da¿o banco de dados
        for row in data5:
            print(row)

    

    connection.commit() # sempre deve commitae tudo para ser alterado no banco de dados

