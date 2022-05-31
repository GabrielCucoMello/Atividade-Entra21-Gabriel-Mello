from linecache import clearcache
from turtle import clear


def id(*args, **kargs):
    for n in args:
        nome = n
        print(f'{n}')

        for k, v in kargs.items():
            idade = k
            sexo = v
            print(f'{idade}, {sexo}')
            print(f'Nome: {nome}, {idade}, {sexo}')


id('Gabriel', idade=18, sexo='M')
