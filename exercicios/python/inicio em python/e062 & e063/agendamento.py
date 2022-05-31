from cadastro_plano_de_saude import user
from banco_de_dados import medicos

def menu():
    menu = str(
        input('Deseja agendar uma consulta? ([S] ou [N])\n')).upper().strip()

    if menu == 'S':
        # paciente = input('Por favor, digite seu nome completo: ')
        print(f'Paciente:  {user}. \nEscolha com qual médico deseja consultar')
        print(f'1- {medicos[0]};')
        print(f'2- {medicos[1]}')

        medico = int(input('Com qual médico desejas agendar uma consulta?\n'))
        if medico == 1:
            print(f'Sua consulta com o(a) {medicos[0]} será agendada')

        if medico == 2:
            print(f'Sua consulta com o(a) {medicos[1]} será agendada')
    else:
        print('Agradecemos seu contato!')