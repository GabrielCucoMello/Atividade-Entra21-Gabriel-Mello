carrinho = []

carrinho.append(('Batata', 3))
carrinho.append(('Feijão', 10))
carrinho.append(('Arroz', 5))
carrinho.append(('Óleo de Soja', 7))
carrinho.append(('Tomate', 5))

total = 0

for produtos in carrinho:
    total = total + produtos[1]

print(f'O total é de R$ {total}')