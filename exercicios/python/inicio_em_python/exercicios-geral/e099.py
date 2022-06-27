class Carros():
    def __init__(self, marca, modelo, ano, cor, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor

    def descricao(self):
        descricao_carro = f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}, Valor: {self.valor}.'
        return descricao_carro


carro1 = Carros('Toyota', 'Supra', '1993', 'Renaissance Red', 'R$ 1.000.000')
carro2 = Carros('Nissan', 'Skyline R34 GTR', '1999', 'Midnight Purple 3', 'R$ 1.652.000')
carro3 = Carros('Chevrolet', 'Opala SS', '1974', 'Vermelho', 'R$ 250.000')

print(carro1)
print(carro2)
print(carro3)

print(carro1.descricao())
print(carro2.descricao())
print(carro3.descricao())