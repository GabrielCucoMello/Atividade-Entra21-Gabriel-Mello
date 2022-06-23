
# numeros = input("digite numeros separados por virgula")

numeros = '0,2,3,9,7,1,5,4,8,12,14'
# numeros = str([ x for x in [0,2,3,9,7,1,5,4,8]])
print(numeros)

lista = numeros.split(',')
lista.sort()

print(lista)