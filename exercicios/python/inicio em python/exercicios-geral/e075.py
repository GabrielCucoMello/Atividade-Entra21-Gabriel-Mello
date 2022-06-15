from multiprocessing.sharedctypes import Value


def divisao(num):
    return [num // 2, num - num // 2]

try:
    n = int(input('Digite um número: '))
    print(divisao(n))
except ValueError:
    print('Valor digitado não é um número.')