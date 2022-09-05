import mysql.connector, pandas as pd, random, sqlite3


cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g4',
    password = 'e2122g4@16@ago',
    database = 'e2122g4'
    )

cur = cnx.cursor()

cur.execute("ALTER TABLE CLIMA ADD PRIMARY KEY (CLIMA_ID)")

cnx.close()