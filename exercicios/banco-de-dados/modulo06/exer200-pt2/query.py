import sqlite3

cnx = sqlite3.connect('exer200pt2.sqlite3')
cur = cnx.cursor()

# cur.execute('SELECT * FROM CIDADES;')
# todas = cur.fetchall()
# print(f'Todas as Cidades: {todas}')

# for x, y, z in todas:
#     print(f'{x}:{y}:{z}')

# cur.execute('SELECT * FROM PESSOAS;')
# todos = cur.fetchall()
# for x, y, z, a in todos:
#     print(f'{x}:{y}:{z}:{a}')

# for i in ['PESSOAS', 'CIDADES']:
#     sql = 'SELECT COUNT(*) FROM ' + i
#     cur.execute(sql)
#     result = cur.fetchall()
#     print(f'{i}:{result}')

cur.execute('''
    SELECT PESSOA_NOME, CIDADE_NOME FROM PESSOAS, CIDADES
    WHERE PESSOA_CIDADE_ID = CIDADE_ID;
''')
resultado = cur.fetchall()
print(f'Todas as linhas Nome e Cidade: {resultado}')