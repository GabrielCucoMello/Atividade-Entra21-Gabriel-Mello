from funcionarios.data import geraData_funcionarios

data = geraData_funcionarios()

def geraData_mult_funcionarios():
    data_mult_funcionarios = []
    loop = 0

    while loop < 1096:
        data_mult_funcionarios.extend([data[loop]] * 90)
        loop += 1
    return data_mult_funcionarios