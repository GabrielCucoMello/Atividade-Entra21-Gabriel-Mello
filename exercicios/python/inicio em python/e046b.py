cadastro = { 
    'Nome': input('Digite seu nome: '),
    'Sexo': input('Digite seu sexo: '),
    'Idade': int(input('Digite sua idade: ')),
    'Nacionalidade': input('Digite sua nacionalidade: '),
    'Estado Civil': input('Digite seu estado civil: '),
    'Escolaridade': [input('Digite sua escolaridade: '), input('Digite seu diploma: ')],
    'Ocupação': input('Digite sua ocupação: ')
}


print(cadastro)