from banco_de_dados import usuarios

user = str(input('Digite seu nome de usuário: '))
# indices = [x for x, y in usuarios.items() if user == y]
# if indices:
#     print('Usuário cadastrado, prosseguindo para o agendamento!')
# else:
#     print('Usuário não cadastrado, cancelando o agendamento.')
#     exit()

#As maneiras de cima e de baixo dão o mesmo resultado.

if user in usuarios.values():
   print('Usuário cadastrado, prosseguindo com o agendamento!')
   pass
else:
   print('Usuário não existe, cancelando agendamento.')
   exit()