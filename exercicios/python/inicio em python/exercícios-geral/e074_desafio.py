class Calculadora:
    result = 0

    def __init__(self, op, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        _f = str(num1) + str(self.op) + str(num2)
        self.result = eval(_f)
    
    #Getter
    @property
    def op(self):
        return self.op_valido
    
    #Setter
    @op.setter
    def op(self, op):
        if isinstance(op, str):
            op = str(op.replace('X' and '.', '*'))
        if isinstance(op, str):
            op = str(op.replace('^', '**'))
            
        self.op_valido = op

num1 = int(input('Digite um primeiro número para ser calculado: '))
op = input('Informe o operador: ').upper()
num2 = int(input('Digite um segundo número para ser calculado: '))

resultado = Calculadora(op, num1, num2)
print(f'Resultado: {resultado.num1} {resultado.op} {resultado.num2} = {resultado.result}')