nomes = []

num = input('Digite alguns nomes separados por vírgula: ')
nomes.append(sorted(num.split(',')))

print('Aqui estão os nomes digitados sortidos: ')
print(nomes)