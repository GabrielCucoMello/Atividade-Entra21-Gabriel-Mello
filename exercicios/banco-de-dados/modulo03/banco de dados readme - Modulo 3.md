video 019
Definição

SQL = Linguagem de comunicação com o Banco de Dados
SQL = Structured Query Language

"Conversa com o banco de dados"
CLIENT -> SERVER

QUAL O CLIENTE CODIGO 1 -->
<-- Adriano

O que conseguimos fazer com SQL:

Criar e Modificar:
- Banco de dados;
- Tabelas;
- Permissões de Acesso;
- Registros de dados;
- Gerenciar Transações: Confirmar ou Desfazer;

video 020:
Organização

DDL - Criação/Manutenção de tabelas
- CREATE 
- ALTER
- DROP (excluir)

DCL - Controle de dados
- GRANT
- REVOKE

DTL - Gerenciamento de Transações
- BEGIN
- COMMIT
- ROLLBACK

DML - Manipulação de Dados
- INSERT
- UPDATE
- DELETE

DQL - Consulta (QUERY)
- SELECT

video 021
DDL - Criação/Manutenção de tabelas

DDL - Data Definition Language  ou Linguagem de Definição de Dados

- Criamos uma estrutura pela ide app https://app.quickdatabasediagrams.com/

IDE:
'''
Pessoas
- 
ID INT PK
CPF TEXT
NOME TEXT
IDADE INT
'''

SQL:
'''
CREATE TABLE `Pessoas` (
    `ID` INT  NOT NULL ,
    `CPF` TEXT  NOT NULL ,
    `NOME` TEXT  NOT NULL ,
    `IDADE` INT  NOT NULL ,
    PRIMARY KEY (
        `ID`
    )
);
'''

video 022:
Mais opções para os atributos de nossa Tabela ou Entidade: Pessoas:

Versão para SqLite
CREATE TABLE PESSOAS{
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	CPF TEXT,
	NOME TEXT NOT NULL,
	IDADE INTEGER
}

1. Criando uma tabela chamada pessoas e utilizando a declaração create
CREATE TABLE PESSOAS{
}

2. Cria o atributo ID do tipo INTEGER, é uma PK, Auto Incremento.
	ID INTEGER PRIMARY KEY AUTOINCREMENT,

3. Criando um atributo chamado CPF do tipo TEXT
	CPF TEXT,

4. Criando um atributo chamado NOME do tipo TEXT, não aceita que seja NULO
	NOME TEXT NOT NULL,

5. Criando um atributo chamado IDADE, tipo INTEGER (Inteiro)
	IDADE INTEGER
	
video 023:
INSERIR dados em uma ENTIDADE

SQL INSERT INTO

CPF, NOME, IDADE

INSERT INTO PESSOAS(CPF, NOME, IDADE)
VALUES
	('123.456.789-00', 'Gabriel Mello', 18),
	('233.567.789-00', 'Tereza Mello', 43);
	
video 024
Criar uma tabela, inserir um registro ao vivo

SQLITE3

video 025

Aqui criamos uma tabela a partir do arquivo pessoas.sql
Falamos aqui o seguinte:
- Cada vez que for eecutado o pessoas.sql, ele vai apagar o conteúdo da tabela e inicializa a tabela novamente. (DROP)
- Tome cuidado com o DROP

video 026

'''
sqlite3 Modulo3.db
sqlite> .read pessoas.sql # este comando, iniciado com . (ponto) é um comando SqLite
sqlite> .schema PESSOAS
CREATE TABLE PESSOAS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CPF TEXT NOT NULL,
    NOME TEXT NOT NULL,
    IDADE INT NOT NULL,
    ENDERECO CHAR(50),
    SALARIO REAL
);
'''

video 027
inserir pessoas na tabela

video 028
select query (DQL)

SELECT * (seleciona todas)
FROM PESSOAS;

video 029
**CUIDADO COM OS COMANDOS UPDATE E DELETE**

UPDATE PESSOAS
    SET SALARIO = 10.00
    WHERE ID = 2;

video 030
**CUIDADO COM ESQUECIMENTOS DO WHERE**

UPDATE PESSOAS 
    SET SALARIO = 10.0;

Nesta condição acima alteramos todos os registros da base, pois esquecemos de colocar o WHERE.

video 031
vamos fazer um delete.

DELETE FROM PESSOAS
    WHERE ID = 2;