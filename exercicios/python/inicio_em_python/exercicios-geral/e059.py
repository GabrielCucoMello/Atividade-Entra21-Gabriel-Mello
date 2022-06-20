def soma(*args):
    num = 0
    for valor in args:
        num += valor
    print(f'O resultado da soma é {num}')


soma = soma(13, 14, 23, 90, 100)
