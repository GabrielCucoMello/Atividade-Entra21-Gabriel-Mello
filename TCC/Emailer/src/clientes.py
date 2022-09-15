import holidays
from datetime import datetime
from src.database_connect import chuva_hoje, data_hoje

feriado_list = []
dia_semana = datetime.today().isoweekday()
clientes_normal = 600
feriado = 0
clientes_final = 0
feriado_check = holidays.Brazil()
if dia_semana == 6 or dia_semana == 7:
    feriado = 1
for i in feriado_check['2022-01-01' : '2022-12-31']:
    feriado_list.append(i.isoformat())
if data_hoje in feriado_list:
    feriado = 1
if feriado == 1:
    consta_feriado = 'Sim'
if feriado == 0:
    consta_feriado = 'Não'
if chuva_hoje >= 23:
    clientes_final = clientes_normal * 0.05
elif chuva_hoje == 23:
    clientes_final = clientes_normal * 0.1
elif chuva_hoje == 22:
    clientes_final = clientes_normal * 0.2
elif chuva_hoje == 21:
    clientes_final = clientes_normal * 0.3
elif chuva_hoje == 20:
    clientes_final = clientes_normal * 0.5
elif chuva_hoje >= 16:
    clientes_final = clientes_normal * 0.6
elif chuva_hoje >= 14:
    clientes_final = clientes_normal * 0.7
elif chuva_hoje >= 13:
    clientes_final = clientes_normal * 0.8
elif chuva_hoje >= 8:
    clientes_final = clientes_normal * 0.9
elif chuva_hoje <= 7:
    clientes_final = clientes_normal

if feriado == 1:
    clientes_final = clientes_final * 2

#colocar match gay