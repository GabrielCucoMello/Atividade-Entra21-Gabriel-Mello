def id(*args,**kwargs):
    for n in args:
        nome = n
        print(f'{n}')
    for k,v in kwargs.items():
        idade = k
        sexo = v
        print(f'{idade},{sexo}')                
id('Adriano', idade='47',sexo='Masculino')
