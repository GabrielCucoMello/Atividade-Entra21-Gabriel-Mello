import datetime
import time

for i in range(15):
    now = datetime.datetime.now()
    print(f'Dia: {now.day}, Mês: {now.month}, Ano: {now.year}, Hora: {now.strftime("%H:%M:%S")}')
    time.sleep(1)