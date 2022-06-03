class Items():
    def __init__(self, item, preco):
        self.item = item
        self.preco = preco
        print(f'Você adicionou ao seu carrinho e comprou: {self.item} custando {self.preco} reais')

item1 = Items(str(input('Digite o nome do primeiro item: ')), int(input('Digite o preco do primeiro item: ')))
item2 = Items(str(input('Digite o nome do segundo item: ')), int(input('Digite o preco do segundo item: ')))