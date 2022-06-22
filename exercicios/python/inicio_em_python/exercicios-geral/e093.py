from random import choices

tamanho = 10
valores = range(1, 21)

numeros = [sorted(choices(valores, k=tamanho))]
print(numeros)