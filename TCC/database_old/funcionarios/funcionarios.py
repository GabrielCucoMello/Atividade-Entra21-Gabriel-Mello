from faker import Faker
from funcionarios.data_mult import geraData_mult_funcionarios

data_mult_funcionarios = geraData_mult_funcionarios()

def geraFuncionarios():
    funcionarios = []
    faker = Faker('pt_BR')

    for i in range(len(data_mult_funcionarios)):
        funcionarios.append(f'{faker.first_name()} {faker.last_name()}')
    return funcionarios