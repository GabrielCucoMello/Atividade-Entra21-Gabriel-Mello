video 001 
usos apropriados para sqlite
formato: cliente => servidor
tipos de bancos de dados nesse formato
- Mysql/MariaDB
- Oracle
- PostgreSQL
(Esforçam: Dados compartilhados em ambientes corporativos)
- Estabilidade
- Simultaneidade
- Centralização
- Controle
sqlite nao se sencaixa

SQLITE
- Armazenar dados localmente
- Economia
- Eficiencia
- Confiabilidade
- Independencia
- Simplicidade

SQLITE NAO COMPETE COM OS BANCOS DE DADOS CLIENT/SERVER
COMPETE APENAS COM fopen()

video 002
situações em que o SQLITE funciona bem
**São dispositivos incorporados (embeded devices)**
**Internet das Coisas (IOT)**

- Client/Server ficam em DATACENTERS (geralmente, mais usados)
- SQLITE ficam em dispositivos (geralmente, mais usados)

video 003
continuação do 002 mas focado em FORMATO DE ARQUIVO DO APLICATIVO

SQLITE OFERECE PORTABILIDADE GIGANTESCA
BEM LEVE

Funciona bem em:
- Sites de tráfego baixo (até médio)
(Site SQLITE)[https://www.sqlite.org]

FERRAMENTA COM ALTA COPIABILIDADE, NAO SERVE PRA FICAR DENTRO DO DATACENTER

video 004
Analise de Dados

os dados brutos podem ser importados pelos arquivos tipos .csv e podem ser fatiados/divididos pelo sqlite3

USOS POSSIVEIS

- Análise de LOG de um SITE
- Compilação de métricas de programação
- Análise de resultados experimentais

sqlite tem facil integração com outras linguas de programação

video 005
CACHE PARA DADOS CORPORATIVOS

UMA BASE BUSCA O QUE FOI APROVADO EM UMA OUTRA BASE PRINCIPAL E EXPORTA PARA UM WEBSERVER, bom para o sqlite ser usado nessa situação, economiza bastante

video 006
BANCO DE DADOS DO LADO DO SERVIDOR

- Base principal com bases externas
    - Aplicativo
        - Diversas bases SQLITE por usuário
            - Aplicativo API
                - Diversos usuários

ao inves de uma unica base gigante especifica, usamos uma base intermediária para acessar as informações por usuário, separando as aplicações
uma é a database
uma é a linkagem da database com a base intermediária pra conexao
uma é a base de conexão intermediária do usuário

diminui o custo de conexões

video 007
Transferência de Dados ou Guardar os dados

pode ser utilizado para substituir o zip, ele cria arquivos zip com arquivos dentro
pode ser muito bom armazenar uma copia do banco de dados com o sqlite

Bancos de dados Internos ou Temporários

para alguns programas que tem muitos dados que devem ser peneirados é muito mais rápido e fácil fazer pelo sqlite

- Demos ou testes (exemplo: utilização para demonstração em feiras)
- Educação e Treinamento
- Testes ou extensões de SQL Experimental (protótipos)

video 008
SITUAÇÕES EM QUE UM RDBMS CLIENT/SERVER PODE FUNCIONAR MELHOR

- Aplicativos Client/Server
- Sites de alto volume
- Conjuntos de dados muito grandes
- Alta simultaneidade
sqlite permite infinitas leituras, mas apenas aceita um escritor por vez

video 009
Lista de verificação para escolher o melhor mecanismo de banco de dados para a sua aplicação.

Escolha cliente servidor se:
- Os dados são separados do aplicativo por uma rede
- Muitos escritores simultaneos
- Dados do tipo XXG

Caso contrario:
- Escolha SQLITE

# SQLITE E APLICATIVOS

