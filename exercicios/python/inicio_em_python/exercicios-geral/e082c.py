class Teste:
    jacare = 'amarelo'
    print('2: ', jacare)
    def __init__(self, jacare):
        print('3: ', jacare)
        self.a = jacare


jacare = 'vermelho'

print('1: ', jacare)

Teste('preto')