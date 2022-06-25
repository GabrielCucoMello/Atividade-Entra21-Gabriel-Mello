valor_hora = 29.11
valor_extra = 5

horas = int(input('Digite quantas horas foram trabalhadas neste mês: ')) * valor_hora
horas_extra = int(input('Digite quantas horas extras foram trabalhadas neste mês: ')) * valor_extra

if (horas/valor_hora) + (horas_extra/valor_extra) >= 40:
    valor_final = horas + horas_extra
else:
    valor_final = horas

print(f'Valor do salário base: R$ {horas}')
print(f'Valor total de horas extras trabalhadas: R$ {horas_extra}')
print(f'Valor total do salário com horas extras (Se houver): R${valor_final}')