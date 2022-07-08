-- Este código tem sintaxe para SqLite portanto não funciona em MySql
-- Este arquivo é um SCHEMA de uma tabela de PESSOAS

BEGIN TRANSACTION;
DROP TABLE IF EXISTS PESSOAS;
CREATE TABLE PESSOAS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CPF TEXT NOT NULL,
    NOME TEXT NOT NULL,
    IDADE INT NOT NULL,
    ENDERECO CHAR(50),
    SALARIO REAL
);

INSERT INTO PESSOAS (CPF, NOME, IDADE, ENDERECO, SALARIO)
    VALUES
    ('123.456.789-00', 'Gabriel Mello', 18, 'Manoel Filho', 2114.00),
    ('233.456.789-00', 'Tereza Mello', 43, 'Manoel Filho', 1280.00); 

COMMIT;

SELECT * FROM PESSOAS;