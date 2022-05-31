dic = dict(
        nome = input('Digite seu nome: '),
        sexo= input('Digite seu sexo: '),
        idade = int(input('Digite sua idade: ')),
        nacionalidade = input('Digite sua nacionalidade: '),
        estadoc = input('Digite seu estado civil: '),
        escolaridade = [input('Digite sua escolaridade: '), input('Digite seu diploma: ')],
        ocupacao = input('Digite sua ocupação: ')
)


print(dic)