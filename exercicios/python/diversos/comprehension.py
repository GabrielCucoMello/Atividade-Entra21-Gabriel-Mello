lista = list([1, 2, 3, 6, 9, 10, 12, 13, 15, 4, 5])

nlista = [x for x in lista if x > 5] #apenas números acima do 5

print(nlista)

nlista2 = [x for x in lista if x % 2 == 0] #apenas pares

print(nlista2)