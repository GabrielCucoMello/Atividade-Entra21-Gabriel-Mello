numeros = []

num = input('Digite alguns números separados por vírgula: ')
numeros = [int(val) for val in num.split(',')]

print('Aqui estão os números digitados sortidos: ')
print(sorted(numeros))