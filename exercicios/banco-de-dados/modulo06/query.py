import sqlite3

cnx = sqlite3.connect('modulo06.sqlite3')
cur = cnx.cursor()

# cur.execute('SELECT * FROM CIDADES;')
# resultado = cur.fetchall()
# print(f'\nTodas as linhas: {resultado}')

# print(type(resultado))

# for x, y in resultado:
#     print(f'{x}, {y}')

cur.execute('SELECT * FROM PESSOAS;')
resultado = cur.fetchall()

for x, y, z, a in resultado:
    print(f'{x}, {y}, {z}, {a}')