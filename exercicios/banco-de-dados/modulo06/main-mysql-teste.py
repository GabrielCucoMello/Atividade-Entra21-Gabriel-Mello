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


tabela = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTFNqcurVDuPNbJsRUJOPdg7klahlJHW_djlCs5wBDS64Y_ZAo9G4s7upXIm_-Uld95zvMJdscf59hg/pub?gid=902654424&single=true&output=csv'
lines = pd.read_csv(tabela, index_col=0, header=0)
lines = len(lines)
print(lines)
colunas = list(['Id','Data', 'CPF', 'Nome', 'Idade', 'Cidade_id'])
while contagem <= lines:
    df = pd.read_csv(tabela, index_col=0, header=0, nrows = 1000, skiprows=[x for x in range(inicio, inicio + contagem)], usecols = colunas)
    contagem += 1000
    print(contagem)

    sql=("INSERT INTO CLIENTES (CLIENTE_DATA, CLIENTE_CPF, CLIENTE_NOME, CLIENTE_IDADE, CLIENTE_CIDADE_ID) VALUES (%s,%s,%s,%s,%s) ")
    for index, row in df.iterrows():
        val=(row.Data, row.CPF, row.Nome, row.Idade, row.Cidade_id)    
        cur.execute(sql,val)
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