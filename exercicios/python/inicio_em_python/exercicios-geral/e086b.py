from random import randint

lista1 = []

while len(lista1) != 5:
    r = randint(1, 10)
    if r not in lista1:
        lista1.append(r)

lista2 = [i ** 3 for i in lista1]

print(lista1)
print(lista2)