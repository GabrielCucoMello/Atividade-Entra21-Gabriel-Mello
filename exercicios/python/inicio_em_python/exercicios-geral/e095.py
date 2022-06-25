from operator import itemgetter

data = []

print('Você deverá informar os dados do aluno da seguinte forma: "Nome, nota1, nota2", separados por vírgulas.')
print('Ao terminar de indexar os dados do aluno, apenas dê um enter para encerrar a entrada de dados.')
while True:
    dados = str(input('Digite, primeiramente, o nome do aluno e logo em seguida duas notas do mesmo: ')).replace(' ', '')
    if not dados:
        break
    data.append(tuple(dados.split(',')))

print(sorted(data, key=itemgetter(0, 1, 2)))