video 001 -  banco de dados com python

Introdução a conexão do SQLite com o Python

- Como criar um novo Banco de Dados (Database) com Python
- Como se conectar ao Database
- Como criar tabelas
- Como inserir dados
- Como selecionar dados inseridos

'''
Cidades:
Id
Nome

Pessoas:
id
Nome
Idade
Cidade_id
'''

video 002 criando tabelas com o python

'''
cur.execute("""
    CREATE TABLE .... ();
""")
'''

video 003 inserção de dados

cur.execute('''
    INSERT INTO .... ();
''')

video 004 seleção de dados

'''
cur.fetchone() --> só o primeiro resultado
cur.fetmatch(2) --> os primeiros dois resultados
cur.fetchall() --> todos os resultados
'''

video 005 uso dos resultados de uma query

'''
Resutlados de uma query con.fetchxxx --> Lista
'''

ExercÍcio 200-2-sqlite + pandas + random -> envio do arquivo main.py 
1. Localize na internet uma lista com todos os Municipios do Brasil, 5570 municipios com a Unidade da Federação 
2. Consolide esses dados em um arquivo CSV/sheets.csv 
3. Crie uma tabela CIDADES (ID/UF/CIDADE) 
4. (PANDAS) Importe todos os municipios para dentro desta tabela. 
5. Imprima todos municipios em uma select * from 
6. Imprima um contador do sql count 
7. Localize na Internet uma lista de todos os nomes de pessoas registrados em cartorio, 100787. 
8. Consolide esses dados em um arquivo CSV/sheets.csv 
9. Crie uma tabela PESSOAS (ID,NOME,IDADE,CIDADE_ID) 
10. (PANDASsorrisoImporte todos os municipios para dentro desta tabela utilizando os seguintes criterios: Nome = nome transportados do csv Idade = Range de 0 a 100 (Random) Cidade_id = Range de 1 a Total de municipios na tabela SQL 
11. Imprima todos em uma select * 12. Imprima um contador do sql 13. Imprima lista de 2000 pessoas, ordenada por estado,cidade,idade,nome (vinda do SQL). http://blog.mds.gov.br/redesuas/wp-content/uploads/2018/06/Lista_Munic%C3%ADpios_com_IBGE_Brasil_Versao_CSV.csv https://brasil.io/dataset/genero-nomes/files/