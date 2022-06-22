carrinho = []

carrinho.append(('Batata', 3))
carrinho.append(('Feijão', 10))
carrinho.append(('Arroz', 5))
carrinho.append(('Óleo de Soja', 7))
carrinho.append(('Tomate', 5))

total = sum([y for x, y in carrinho])

print(f'O total é de R$ {total}')