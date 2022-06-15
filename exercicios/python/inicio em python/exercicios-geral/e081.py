from random import choice
import string

passlen = int(input('Digite um tamanho desejado de senha: '))
caracters = string.ascii_letters + string.digits
safepass = ' '
for i in range(passlen):
    safepass += choice(caracters)

print(f'A senha gerada aleatóriamente é: {safepass}')
