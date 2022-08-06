import sqlite3, pandas as pd, random

cnx = sqlite3.connect('exer200pt2.sqlite3')
cur = cnx.cursor()


tabela = ('https://docs.google.com/spreadsheets/d/e/2PACX-1vSGBot2EFAMNJRdwUVK3ou7lC0uQcZE3X9NqUaVJmgd778ZVSJAAVljtZPG3eHEseo2pZQ4HKITGWZ1/pub?gid=536340842&single=true&output=csv')
colunas = list(['ID', 'UF', 'Município'])
df = pd.read_csv(tabela, index_col=0, header=0, usecols=colunas)

cur.execute('''
    DROP TABLE IF EXISTS CIDADES;
''')

cur.execute('''
    CREATE TABLE CIDADES(
        CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CIDADE_NOME TEXT,
        CIDADE_UF TEXT
    );
''')

numcidades = list((df.shape))[0]

sql = ('INSERT INTO CIDADES (CIDADE_UF, CIDADE_NOME) VALUES (?, ?)')
for index, row in df.iterrows():
    val = (row.UF, row.Município)
    cur.execute(sql,val)

cnx.commit()

tabela = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRcfN-GUulEPs47D1rlNvxLO2tkuP-1hkx6e6p6KSIOyBGNgHb3qgW2M45QFiHwJXrNVH5_3DnLsPJX/pub?gid=931200727&single=true&output=csv'
colunas = list(['ID', 'first_name'])
df = pd.read_csv(tabela, index_col=0, header=0, usecols=colunas)

cur.execute('''
    DROP TABLE IF EXISTS PESSOAS;
''')

cur.execute('''
    CREATE TABLE PESSOAS(
        PESSOA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PESSOA_NOME TEXT,
        PESSOA_IDADE INTEGER,
        PESSOA_CIDADE_ID INTEGER
    );
''')


sql = ('INSERT INTO PESSOAS (PESSOA_NOME, PESSOA_IDADE, PESSOA_CIDADE_ID) VALUES (?, ?, ?)')
for index, row in df.iterrows():
    nome = row.first_name
    idade = random.randrange(0, 110)
    cidade_id = random.randrange(1, numcidades)
    val = (nome, idade, cidade_id)
    cur.execute(sql, val)

cnx.commit()
cur.close