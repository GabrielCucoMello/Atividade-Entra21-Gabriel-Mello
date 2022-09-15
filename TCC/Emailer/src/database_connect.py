import mysql.connector


cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )

cur = cnx.cursor()

cur.execute('SELECT * FROM PREVISAO_TRATADA')

data = []
chuva = []
chance_chuva = []

for i in cur:
    data.append(i[1].isoformat())
    chuva.append(i[2])
    chance_chuva.append(i[3])

chuva_hoje = chuva[0]
data_hoje = data[0]
chance_chuva_hoje = chance_chuva[0]