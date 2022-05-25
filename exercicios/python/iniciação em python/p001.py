from pandasfile import importa_planilha

# colunas = list(['id', 'Nome', 'Telefone'])
# dd = importa_planilha(colunas)
# print(dd)

exemplo = 3

print(f'Demonstração do exemplo: {exemplo}')

if (exemplo == 1):
    colunas = list(['id', 'Nome', 'Telefone'])

    dd = importa_planilha(colunas)

    colunas.remove('id')

    for i in dd.items():
        print(f'Items: {i}')

    for i in dd.values():
        print(f'Values: {i}')

if (exemplo == 2):
    colunas = list(['id', 'Nome', 'Telefone'])

    dd = importa_planilha(colunas)
    colunas.remove('id')

    for i in dd.values():
        print(i['Nome'], i['Telefone'])

if (exemplo == 3):
    newdict = []

    colunas = list({'id', 'Nome', 'Telefone', 'CEP',
                   'Idade', 'N1', 'N2', 'N3', 'N4'})
    colunas.remove('id')

    dd = importa_planilha(colunas)

    colnotas = list({'N1', 'N2', 'N3', 'N4'})

    print('======================================================')
    for x in colunas:
        print(' ', x, end=' ')
    print('\n------------------------------------------------------')

    for i in dd.values():
        print(':', end=' ')

        for N in colunas:
            print(i[N], end=' ')

    somanotas = 0
    numnotas = 0

    for M in colnotas:
        somanotas += float(str(i[M]).replace(',', '.'))
        numnotas += 1
        media = (somanotas/numnotas)
        roundmed = round(media, 2)

    print(f'Soma: {round(somanotas, 1)}, Média: {roundmed}')

    status = 'Reprovado'
    if (roundmed >= 7):
        status = 'Aprovado'

# dando erro, arrumar amanhã: Demonstração do exemplo: 3
# ======================================================
#   CEP   Nome   Idade   Telefone   N2   N4   N3   N1 
# ------------------------------------------------------
# : 89010230 Traceback (most recent call last):
#   File "c:\Users\cucom\Desktop\curso\Atividade-Entra21-Gabriel-Mello\exercicios\python\iniciação em python\p001.py", line 53, in <module>
#     print(i[N], end=' ')
# KeyError: 'Nome'