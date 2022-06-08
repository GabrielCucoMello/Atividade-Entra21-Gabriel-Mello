class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def ano_nascimento(self):
        ano_nasc = self.ano_atual - self.idade
        print(f'Seu ano de nascimento é {ano_nasc}')


p1 = Pessoa(str(input('Digite seu nome: ')), int(input('Digite sua idade: ')))
print(p1.ano_nascimento())
