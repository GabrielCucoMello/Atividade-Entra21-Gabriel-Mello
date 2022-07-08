-- SELECT * FROM PESSOAS;

-- SELECT * FROM CIDADES;

-- SELECT PESSOA_NOME, PESSOA_IDADE FROM PESSOAS;

-- SELECT DISTINCT PESSOA_NOME FROM PESSOAS;

-- SELECT * FROM PESSOAS WHERE PESSOA_IDADE IN (13, 18);

-- SELECT * FROM PESSOAS WHERE PESSOA_NOME LIKE '%Gabriel%';

-- SELECT * FROM PESSOAS WHERE PESSOA_NOME LIKE '%Pedro%' AND PESSOA_IDADE = 18;

-- SELECT * FROM PESSOAS WHERE PESSOA_NOME LIKE '%Pedro%' OR PESSOA_IDADE = 18;

-- SELECT * FROM PESSOAS WHERE PESSOA_IDADE BETWEEN 30 AND 50;

-- SELECT PESSOA_IDADE, PESSOA_NOME FROM PESSOAS ORDER BY PESSOA_IDADE;

-- SELECT PESSOA_IDADE, PESSOA_NOME FROM PESSOAS ORDER BY PESSOA_IDADE, PESSOA_NOME;

-- SELECT PESSOA_IDADE, PESSOA_NOME FROM PESSOAS ORDER BY PESSOA_IDADE DESC;

-- SELECT AVG(PESSOA_IDADE) FROM PESSOAS;

-- SELECT MIN(PESSOA_IDADE) FROM PESSOAS;

-- SELECT MAX(PESSOA_IDADE) FROM PESSOAS;

-- SELECT SUM(PESSOA_IDADE) FROM PESSOAS;

-- SELECT COUNT(*) FROM PESSOAS;

-- SELECT PESSOA_IDADE, COUNT(PESSOA_NOME) 
-- FROM PESSOAS
-- GROUP BY PESSOA_IDADE;

-- SELECT 
--     CIDADES.CIDADE_NOME,
--     PESSOAS.PESSOA_NOME,
--     PESSOAS.PESSOA_IDADE
-- FROM
--     PESSOAS, CIDADES
-- WHERE
--     PESSOAS.PESSOA_CIDADES_ID = CIDADES.CIDADE_ID;