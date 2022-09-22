from chuva_clientes.chuva import geraClientes
from chuva_clientes.data import geraData

clientes = geraClientes()
data = geraData()

def geraDataTotal():
    data_mult = []
    loop = 0

    while loop < 1096:
        data_mult.extend([data[loop]] * clientes[0][loop])
        loop += 1
    return data_mult