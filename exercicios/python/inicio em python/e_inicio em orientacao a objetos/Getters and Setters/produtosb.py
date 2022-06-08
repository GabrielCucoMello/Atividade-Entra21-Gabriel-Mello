class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))

    #Getter
    @property
    def preco(self):
        return self.preco_valido
    
    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ' '))
        self.preco_valido = valor

produto1 = Produto('Cadeira Gamer', 1600)
print(produto1.preco)
produto1.desconto(10)
print(produto1.preco)

produto2 = Produto('Mouse', 450)
print(produto2.preco)
produto2.desconto(20)
print(produto2.preco)

produto3 = Produto('Teclado Gamer', 'R$ 800')
print(produto3.preco)
produto3.desconto(20)
print(produto3.preco)