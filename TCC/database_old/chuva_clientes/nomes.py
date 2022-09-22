from faker import Faker
from chuva_clientes.chuva import geraClientes

clientes = geraClientes()

def geraNomes():
    nomes = []
    faker = Faker('pt_BR')

    for i in range(sum(clientes[0])):
        nomes.append(f'{faker.first_name()} {faker.last_name()}')
    return nomes