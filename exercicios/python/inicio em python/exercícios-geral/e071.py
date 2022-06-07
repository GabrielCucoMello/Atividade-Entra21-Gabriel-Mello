class Calculadora():

    def soma(self, p1, p2):
        return p1 + p2
    
    def sub(self, p1, p2):
        return p1 - p2
    
    def mult(self, p1, p2):
        return p1 * p2
    
    def div(self, p1, p2):
        return p1 / p2


contas = Calculadora()

print(contas.soma(3, 4))
print(contas.sub(4, 3))
print(contas.mult(3, 4))
print(contas.div(12, 4))

# eval, testar depois