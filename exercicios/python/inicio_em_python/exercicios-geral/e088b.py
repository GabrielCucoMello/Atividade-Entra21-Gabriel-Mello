class Quadrado():
    def __init__(self, num):
        self.num = num ** 2
        print(self.num)
    
quant_num = int(input('Digite um número inteiro: '))
quad = Quadrado(quant_num)