import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )

cur = cnx.cursor()


cur.execute("""
    DROP TABLE IF EXISTS CLIMA; 
""")

cur.execute("""    
    CREATE TABLE CLIMA (
            CLIMA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            CLIMA_DATA TEXT NOT NULL,
            CLIMA_CHUVAMM INTEGER,
            CLIMA_TEMPMIN FLOAT NOT NULL,
            CLIMA_TEMPMAX FLOAT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS CLIENTES; 
""")

cur.execute("""
    CREATE TABLE CLIENTES(
        CLIENTE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        CLIENTE_DATA TEXT NOT NULL,
        CLIENTE_CPF TEXT NOT NULL,
        CLIENTE_NOME TEXT NOT NULL,
        CLIENTE_IDADE INTEGER NOT NULL,
        CLIENTE_CIDADE_ID INTEGER NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS FUNCIONARIOS; 
""")

cur.execute("""
    CREATE TABLE FUNCIONARIOS(
        FUNCIONARIO_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        FUNCIONARIO_DATA TEXT NOT NULL,
        FUNCIONARIO_NOME TEXT NOT NULL, 
        FUNCIONARIO_ATRACOES_ID INTEGER NOT NULL
        );
""")

cur.execute("""
    DROP TABLE IF EXISTS ATRACOES; 
""")

cur.execute("""    
    CREATE TABLE ATRACOES (
            ATRACAO_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            ATRACAO_NOME TEXT NOT NULL,
            ATRACAO_SETOR TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

cur.execute("""    
    CREATE TABLE CIDADES (
            CIDADE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            CIDADE_UF TEXT NOT NULL,
            CIDADE_NOME TEXT NOT NULL
    );
""")

#Tabela Funcionarios
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRPs43CE0ejjDVZ3fyEuuZ83pNeZPfF69Z3wVcGO41NydqQbmzBGH9WwzT9ht4IswElmjawq-gW8G92/pub?gid=164424013&single=true&output=csv'
colunas = list(['id','data','nome','atracao_id'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
sql=("INSERT INTO FUNCIONARIOS (FUNCIONARIO_DATA, FUNCIONARIO_NOME, FUNCIONARIO_ATRACOES_ID) VALUES (%s,%s,%s) ")
for index, row in df.iterrows():
    val=(row.data, row.nome, row.atracao_id)    
    cur.execute(sql,val)
cnx.commit()

#Tabela Atracoes
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTy5XJYo9_ZlY8f7lkYcVWPQ-eIOlxR9Phd5f3B0icUHBSs-GrztXYliPbB_skhVlcZXe3BoNkkh94Z/pub?gid=2053312388&single=true&output=csv'
colunas = list(['ID','NOME','SETOR'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
sql=("INSERT INTO ATRACOES (ATRACAO_NOME, ATRACAO_SETOR) VALUES (%s,%s) ")
for index, row in df.iterrows():
    val=(row.NOME, row.SETOR)    
    cur.execute(sql,val)
cnx.commit()

#Tabela Clima
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTjH6P-tb9WAqEZUeGAGCAhmLANbm3qZ4-6dKfT7aTbZlq8Zh8aO6i-9egMOLKIjdicBMTavZob0ISe/pub?gid=1327518476&single=true&output=csv'
colunas = list(['Id','Data', 'Chuva', 'Tempmin', 'Tempmax'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
sql=("INSERT INTO CLIMA (CLIMA_DATA, CLIMA_CHUVAMM, CLIMA_TEMPMIN, CLIMA_TEMPMAX) VALUES (%s,%s,%s,%s) ")
for index, row in df.iterrows():
    val=(row.Data, row.Chuva, row.Tempmin, row.Tempmax)    
    cur.execute(sql,val)
cnx.commit()

#Tabela Clientes
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTFNqcurVDuPNbJsRUJOPdg7klahlJHW_djlCs5wBDS64Y_ZAo9G4s7upXIm_-Uld95zvMJdscf59hg/pub?gid=902654424&single=true&output=csv'
colunas = list(['Id','Data', 'CPF', 'Nome', 'Idade', 'Cidade_id'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
sql=("INSERT INTO CLIENTES (CLIENTE_DATA, CLIENTE_CPF, CLIENTE_NOME, CLIENTE_IDADE, CLIENTE_CIDADE_ID) VALUES (%s,%s,%s,%s,%s) ")
for index, row in df.iterrows():
    val=(row.Data, row.CPF, row.Nome, row.Idade, row.Cidade_id)    
    cur.execute(sql,val)
cnx.commit()

#Tabela Cidades
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSqpxiXuROqjtAI24wP7WSLvg6YlwOHKfQASvXZ3I-zRmxCW6Q2oDx_IG8uT0rdIBUxomunDyURxW-G/pub?gid=385229407&single=true&output=csv'
colunas = list(['ID','UF', 'Município'])
df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
sql=("INSERT INTO CIDADES (CIDADE_UF, CIDADE_NOME) VALUES (%s,%s) ")
for index, row in df.iterrows():
    val=(row.UF, row.Município)    
    cur.execute(sql,val)
cnx.commit()

cur.close
