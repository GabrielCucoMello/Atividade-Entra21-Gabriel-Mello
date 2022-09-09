import mysql.connector, pandas as pd, random, sqlite3


# cnx = sqlite3.connect('exer200pt2.sqlite3')

cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )

cur = cnx.cursor()

# def tamanhotabela(df):
#     return(len(df))

# def readcsvcid(tabela):
#     tabela = ''
#     colunas = list(['ID', 'UF', 'Município'])
#     df = pd.read_csv(tabela, index_col=0, header=0, skiprows=(inicio, tamanhotabela(df), tamanho), nrows=tamanho, usecols=colunas)

# def tamtabela(tabela):
#     df1 = pd.read_csv(tabela)
#     tam = len(df1)
#     return tam
    
# def lertabela(tabela):
#     colunas = list(['ID', 'UF', 'Município'])
#     df = pd.read_csv(tabela,  index_col=0, header=0, nrows=tamanho, usecols=colunas)
#     return df

contagem = 0
inicio = 1
# passos = 10
# sair = False

# cur.execute("""
#     ALTER TABLE CLIENTES ADD CLIENTE_DATA TEXT NOT NULL;
# """)


tabela = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTt78dVu4S5AJmccyTrVzZYaX1Xakc9OEmkcwFFSgJf0YkC_POAmGnrCufFgILQuKqXwd-RKwv75nCv/pub?output=csv'
while contagem <= 572238:
    df = pd.read_csv(tabela, index_col=0, header=0, nrows = 1000, skiprows=[x for x in range(inicio, inicio + contagem)], usecols = ['id', 'ajuda'])
    print(df)
    contagem += 1000
    print(contagem)

    values = []
    for index,row in df.iterrows():
        data = row.ajuda
        values.append((data))
            
    insert_values = "".join(str(values).strip('[]'))
    sql=(f"INSERT INTO CLIENTES (CLIENTE_DATA) VALUES {insert_values}")
    cnx.commit()
cnx.close()

# tabela = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRcfN-GUulEPs47D1rlNvxLO2tkuP-1hkx6e6p6KSIOyBGNgHb3qgW2M45QFiHwJXrNVH5_3DnLsPJX/pub?gid=931200727&single=true&output=csv'
# colunas = list(['ID', 'first_name'])
# df = pd.read_csv(tabela, index_col=0, header=0, nrows=tamanho, usecols=colunas)
# numpessoas = list((df.shape))[0]

# cur.execute('''
#     DROP TABLE IF EXISTS PESSOAS;
# ''')

# cur.execute('''
#     CREATE TABLE PESSOAS(
#         PESSOA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
#         PESSOA_NOME TEXT,
#         PESSOA_IDADE INTEGER,
#         PESSOA_CIDADE_ID INTEGER
#     );
# ''')


# sql = ('INSERT INTO PESSOAS (PESSOA_NOME, PESSOA_IDADE, PESSOA_CIDADE_ID) VALUES (?, ?, ?)')
# for index, row in df.iterrows():
#     nome = row.first_name
#     idade = random.randrange(0, 110)
#     cidade_id = random.randrange(1, tamanhotabela_cidades)
#     val = (nome, idade, cidade_id)
#     cur.execute(sql, val)

# cnx.commit()
cur.close