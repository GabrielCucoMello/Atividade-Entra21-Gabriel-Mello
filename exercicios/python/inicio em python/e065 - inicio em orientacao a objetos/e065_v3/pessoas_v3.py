class Pessoa:
    def __init__(self, nome, idade, sexo=False, altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

pessoa1 = Pessoa('Gabriel Mello', 18, 'M', 1.83)
pessoa2 = Pessoa('Karina', 45)

print(pessoa1.nome, pessoa1.idade, pessoa1.sexo, pessoa1.altura)
print(pessoa2.nome, pessoa2.idade, pessoa2.sexo, pessoa2.altura)