BEGIN TRANSACTION;
DROP TABLE IF EXISTS PRODUTOS;
CREATE TABLE PRODUTOS(
    PRODUTO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PRODUTO_NOME TEXT NOT NULL,
    PRODUTO_VALOR_UNITARIO INTEGER NOT NULL
);

DROP TABLE IF EXISTS PRATELEIRAS;
CREATE TABLE PRATELEIRAS(
    PRATELEIRA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PRATELEIRA_NOME TEXT NOT NULL,
    PRATELEIRA_LOCALIZACAO TEXT NOT NULL
);

DROP TABLE IF EXISTS NOTAS;
CREATE TABLE NOTAS(
    NOTA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOTA_NOME TEXT NOT NULL,
    PRATELEIRAS_LOCALIZACAO TEXT NOT NULL,
);


COMMIT;