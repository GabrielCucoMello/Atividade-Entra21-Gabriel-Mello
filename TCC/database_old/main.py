from chuva_clientes.chuva import geraClientes
from chuva_clientes.data import geraData
from chuva_clientes.nomes import geraNomes
from chuva_clientes.cpf import geraCpf_lista
from chuva_clientes.cidades_cont import geraCidades_id
from chuva_clientes.idade import geraIdade
from chuva_clientes.data_total import geraDataTotal
from atracoes.atracoes import GeradorDeAtracoesSetor
from funcionarios.data_mult import geraData_mult_funcionarios
from funcionarios.funcionarios import geraFuncionarios
import mysql.connector, pandas as pd, sqlite3

# FORMATADO PRA ENVIAR PARA UM SQLITE3, PARA NAO DERRUBAR NADA DA NUVEM


atracao = [x for x in range(1, 19)]
atracao = atracao * 5480

clientes_chuva = geraClientes()

atracoes = GeradorDeAtracoesSetor()
atracoes.GeraAtracoes()

contagem_clientes = 0
contagem_clima = 0
contagem_atracao = 0
contagem_funcionarios = 0
passos_clientes = 100000
passos_clima = 100
passos_atracao = 10
passos_funcionarios = 10000



cnx = sqlite3.connect('DATABASE.sqlite3')

# cnx = mysql.connector.connect(
#     host = '3.89.36.150',
#     user = 'e2122g4',
#     password = 'e2122g4@16@ago',
#     database = 'e2122g4'
#     )

cur = cnx.cursor()


cur.execute('''
    DROP TABLE IF EXISTS CLIENTES;
''')

cur.execute('''
    CREATE TABLE CLIENTES(
        CLIENTE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CLIENTE_NOME TEXT NOT NULL,
        CLIENTE_IDADE INTEGER NOT NULL,
        CLIENTE_DATA DATE NOT NULL,
        CLIENTE_CPF TEXT NOT NULL,
        CLIENTE_CIDADE_ID INTEGER NOT NULL
    );
''')

cur.execute('''
    DROP TABLE IF EXISTS CLIMA;
''')

cur.execute('''
    CREATE TABLE CLIMA(
        CLIMA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CLIMA_DATA DATE NOT NULL,
        CLIMA_CHUVA_MM INTEGER NOT NULL
    );
''')

cur.execute('''
    DROP TABLE IF EXISTS ATRACOES;
''')

cur.execute('''
    CREATE TABLE ATRACOES(
        ATRACAO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ATRACAO_NOME TEXT NOT NULL,
        ATRACAO_SETOR TEXT NOT NULL
    );
''')


cur.execute('''
    DROP TABLE IF EXISTS FUNCIONARIOS;
''')

cur.execute('''
    CREATE TABLE FUNCIONARIOS(
        FUNCIONARIO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FUNCIONARIO_NOME TEXT NOT NULL,
        FUNCIONARIO_DATA DATE NOT NULL,
        FUNCIONARIO_ATRACAO_ID INTEGER NOT NULL
    );
''')

cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

cur.execute("""    
    CREATE TABLE CIDADES(
            CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CIDADE_UF TEXT NOT NULL,
            CIDADE_NOME TEXT NOT NULL
    );
""")

clientes_final = list(zip(geraNomes(), geraIdade(), geraDataTotal(), geraCpf_lista(), geraCidades_id()))
data_final = list(zip(geraData(), clientes_chuva[1]))
atracao_final = list(zip(atracoes.atracoes, atracoes.setor))
funcionarios = list(zip(geraFuncionarios(), geraData_mult_funcionarios(), atracoes.atracoes))

print(len(clientes_final))
print(len(data_final))


# while contagem_clientes < sum(clientes_chuva[0]):
#     cur.executemany('INSERT INTO CLIENTES (CLIENTE_NOME, CLIENTE_IDADE, CLIENTE_DATA, CLIENTE_CPF, CLIENTE_CIDADE_ID) VALUES (?, ?, ?, ?, ?)', clientes_final[contagem_clientes: passos_clientes])
#     contagem_clientes += 100000
#     passos_clientes += 100000
#     cnx.commit()
#     print('Adição de 100 mil registros de CLIENTES completa.')

# while contagem_clima < len(data_final):
#     cur.executemany('INSERT INTO CLIMA (CLIMA_DATA, CLIMA_CHUVA_MM) VALUES (?, ?)', data_final[contagem_clima: passos_clima])
#     contagem_clima += 100
#     passos_clima += 100
#     cnx.commit()
#     print('Adição de 100 registros de CHUVA completa.')

# while contagem_atracao < len(atracoes.atracoes):
#     cur.executemany('INSERT INTO ATRACOES (ATRACAO_NOME, ATRACAO_SETOR) VALUES (?, ?)', atracao_final[contagem_atracao: passos_atracao])
#     contagem_atracao += 10
#     passos_atracao += 10
#     cnx.commit()
#     print('Adição de 10 registros de ATRACOES completa.')

# while contagem_funcionarios < len(geraData_mult_funcionarios()):
#     cur.executemany('INSERT INTO FUNCIONARIOS (FUNCIONARIO_NOME, FUNCIONARIO_DATA, FUNCIONARIO_ATRACAO_ID) VALUES (?, ?, ?)', funcionarios[contagem_funcionarios: passos_funcionarios])
#     contagem_funcionarios += 10000
#     passos_funcionarios += 10000
#     cnx.commit()
#     print('Adição de 10000 registros de FUNCIONARIOS completa.')

# cidades = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSqpxiXuROqjtAI24wP7WSLvg6YlwOHKfQASvXZ3I-zRmxCW6Q2oDx_IG8uT0rdIBUxomunDyURxW-G/pub?gid=385229407&single=true&output=csv'
# colunas = list(['ID','UF', 'Município'])
# df = pd.read_csv(cidades, index_col=0, header=0, usecols=colunas)
# sql=("INSERT INTO CIDADES (CIDADE_UF, CIDADE_NOME) VALUES (?, ?) ")
# for index, row in df.iterrows():
#     val=(row.UF, row.Município)
#     cur.execute(sql,val)
# cnx.commit()
# print('Adição da tabela de CIDADES completa.')
# cnx.close()