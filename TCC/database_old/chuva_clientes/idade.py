from random import randint
from chuva_clientes.chuva import geraClientes

clientes = geraClientes()

def geraIdade():
    idade = []
    loop = 0

    while loop < (sum(clientes[0])):
        idade.append(randint(1, 110))
        loop += 1
    return idade