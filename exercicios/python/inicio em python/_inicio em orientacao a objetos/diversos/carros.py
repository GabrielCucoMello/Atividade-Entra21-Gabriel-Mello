class Carros:
    nome = 'Default'

    def __init__(self):
        self.nome = 'Nissan GTR'

print(Carros.nome)

carro = Carros()

print(carro.nome)