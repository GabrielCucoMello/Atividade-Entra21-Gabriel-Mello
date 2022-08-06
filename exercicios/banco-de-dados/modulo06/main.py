import sqlite3

cnx = sqlite3.connect('modulo06.sqlite3')
cur = cnx.cursor()

cur.execute('''
    DROP TABLE IF EXISTS CIDADES;
''')

cur.execute('''
    CREATE TABLE CIDADES(
        CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CIDADE_NOME TEXT NOT NULL
    );
''')


cur.execute('''
    DROP TABLE IF EXISTS PESSOAS;
''')

cur.execute('''
    CREATE TABLE PESSOAS(
        PESSOA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PESSOA_NOME TEXT NOT NULL,
        PESSOA_IDADE INTEGER,
        PESSOA_CIDADE_ID INTEGER NOT NULL
    );
''')

cur.execute('''
    INSERT INTO CIDADES (CIDADE_NOME) VALUES
    ('Curitiba'),
    ('Blumenau'),
    ('Florianopolis'),
    ('Sao Jose'),
    ('Campo Largo');
''')

cur.execute('''
    INSERT INTO PESSOAS(PESSOA_NOME, PESSOA_IDADE, PESSOA_CIDADE_ID)
        VALUES
            ('Gabriel Mello', 18, 4),
            ('Adriano Machado', 47, 2),
            ('Felipe Luiz', 30, 1),
            ('Luiz Calo', 50, 3),
            ('Pedro Lucas', 13, 1),
            ('Pedro Lucas', 18, 2),
            ('Arnaldo Sarce', 18, 3);
''')

cnx.commit()

# Fetchone()

# cur.execute('SELECT * FROM CIDADES;')
# primeiro_resultado = cur.fetchone()
# print(f'\nPrimeira linha: {primeiro_resultado}')

# Fetchmany(2)

# cur.execute('SELECT * FROM CIDADES;')
# resultado = cur.fetchmany(2)
# print(f'\nPrimeiras duas linha: {resultado}')

# Fetchall()

# cur.execute('SELECT * FROM CIDADES;')
# resultado = cur.fetchall()
# print(f'\nTodas as linhas: {resultado}')

cur.execute('''
    SELECT PESSOA_NOME, CIDADE_NOME FROM PESSOAS,CIDADES
        WHERE PESSOA_CIDADE_ID = CIDADE_ID;
''')
resultado = cur.fetchall()
print(f'\nTodas as linhas Nome e Cidade: {resultado}')
