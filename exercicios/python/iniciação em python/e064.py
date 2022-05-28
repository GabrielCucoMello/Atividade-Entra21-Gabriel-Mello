num = list([18, 2004, 2022])
data = {
    'Nome': 'Gabriel',
    'Profissão': 'Expeditor'
}

def id(*args, **kargs):
    print(args)
    print(kargs)
    print(kargs['Nome'])
    print(kargs['Profissão'])

id(*num, **data)