Modulo 01 - Aula 01 - O que é Banco de Dados
video 001
O que é?
Conjunto de informações organizadas em um formato onde os dados possam ser facilmente:
Armazenados.
gerenciados.
atualizados.
recuperados.
Tipos de Bancos de Dados?
Categorias (duas):
Banco de dados Relacional
Banco de dados Não relacional (NoSQL)

Modulo 01 - Aula 02 - Estrutura de um Banco de Dados
video 002
Banco de Dados Relacional: Caracterizado pela forma como os dados são organizados.
Tabelas respeitam um SCHEMA Determina como as tabelas devem ser. Estrutura fixa.
Tabelas ou Entidade
: id : cpf : nome : idade : 
: 1 : 123.456.789-11 : Adriano : 18 : 
: 2 : 123-555-777-12 : Karina : 40 :

Colunas ou Atributos: Unidade que armazena um tipo de valor específico
Linhas ou Tuplas: Representa todos os dados de uma ocorrência na tabela
Cada coluna vai ter apenas um tipo de dado.

video 003
Tipos de Dados:
Text
Integer
Real
Null:
https://www.sqlite.org/datatype3.html

video 004
Chave Primaria - PK Primary Key - Ela serve para definir exclusividades dentro de uma tabela. Cada linha de nossa tabela é unica, definida pela PK. Só podemos definir uma unica coluna dentro da tabela como PK. Uma chave primaria pode ser com uma unica coluna ou composta por 2 colunas de nossa tabela.

ID Abreviação de Identificação ID (criar uma sequencia automatica) -> sempre criar no começo dos dados, como PK

Regras:

Deve ser única.
Nao pode mundar nunca.
Não pode ser nula.

video 005
Chave estrangeira (FK) (Foreign Key) Serve de referência para uma PK em outra tabela na qual são relacionadas.

Pessoas: "Tabela 1"+
: id : cpf : nome : cidade : 
: 1 : 123.456.789-11 : Adriano : 1 : 
: 2 : 123-555-777-12 : Karina : 2 : 
: 3 : 322-555-666-11 : Odineia : 1 :

Cidades: "Tabela 2"
: id : Cidade : UF : 
: 1 : Campo Grande : 2 : 
: 2 : Joinville : 1 :

Estado: "Tabela 3"
: id : Estado : 
: 1 : Santa Catarina : 
: 2 : Mato Grosso do Sul :

video 006
Relacionamento entre tabelas / entidades

Relacionamento: associação entre as tabelas, que são conectadas por Chaves Primarias (PK), Chaves Estrangeiras (FK)

1:1 - Relacionamento de 1 linha de uma tabela com 1 linha de outras tabelas
1:N - Relacionamento de 1 linha de um tabela com muitas linhas de outras tabelas
M:N - Relacionamento de muitas linhas de uma tabela com muitas linhas de outras tabelas

1:1 Relacionamento UM para UM

1:1 - Gerentes x Departamentos

Gerentes:
id -  Nome
1  -  Hans
2  -  Fritz

Departamentos:
id -  Nome - Gerente_ID
1  -  Produção - 1
2  -  Marketing - 2

video 007
1:n - Relacionamento Um para Muitos

Marcas:
id - Nome
1 - Dell
2 - Apple

Produtos:
id - Nome - marcas_id
1 - Teclado - 1
2 - Monitor - 1
3 - Iphone 7 - 2
4 - Iphone 8 - 2

video 008
M:N - Relacionamento de Muitos para Muitos

Música:
id - nome
1 - Highway to Hell
2 - Stairway to Heaven
3 - Another Day In Paradise

Autores:
id - nome
1 - Bon Scott
2 - Angus Young
3 - Malcom Younb
4 - Robert Plant
5 - Jimmy Page
6 - Phill Collins

MusicaxAutores
id - musica_id - autores_id
1 - 1 - 1
2 - 1 - 2
3 - 1 - 3
4 - 2 - 4
5 - 2 - 5
6 - 3 - 6

video 009
Auto Relacionamento
Relacionamento de uma linha de uma mesma tabela com outra linha nesta mesma tabela

Pessoas, Mae, Pais

: id : nome    : mae_id : pai_id :
: 1  : Adriano : 4	    : 6		 :
: 2  : Karina  : 4	    : 6		 :
: 3  : Odineia : 5	    : 7		 :
: 4  : Elvira  : 0	    : 0		 :	
: 5  : Maria   : 0	    : 0		 :
: 6  : Carlos  : 0	    : 0		 :
: 7  : Miguel  : 0	    : 0		 :

video 010
Apresentação de DER de um auto-relacionamento (video 009)

