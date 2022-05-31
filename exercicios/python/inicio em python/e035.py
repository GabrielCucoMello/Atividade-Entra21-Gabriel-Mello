numero = int(input('Digite um número: '))
divisoes = 0

# range(start, stop, step)
for i in range (1, numero + 1):
    if numero %i == 0:
        divisoes += 1

if divisoes == 2:
    print(f'{numero} é um número primo!')
    print(f'{numero} é divisível somente por um ou por {numero}')
else:
    print(f'{numero} náo é um número primo!')
    print(f'{numero} é divisível {divisoes} vezes')