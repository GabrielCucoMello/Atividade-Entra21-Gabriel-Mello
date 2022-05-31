def boav(nome, nacionalidade ='Brasileiro'):
    print(f'Olá {nome}, você é {nacionalidade}')

nome = input('Digite seu nome: ')
# ex1 = boav(nome)

nac = input('Digite sua nacionalidade: ')
ex2 = boav(nome, nac)