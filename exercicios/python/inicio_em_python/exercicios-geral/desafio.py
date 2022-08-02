class Calculadora:
    result = 0

    def __init__(self, calc):
        self.calc = calc
        _f = str(calc)
        self.result = eval(_f)

fita = []
result = {}


while True:
    entrada = str(input('Informe o cálculo: ')).strip()
    if entrada[-1] == entrada[-2]:
        op = f'{entrada[-1]}{entrada[-2]}'
        if 'm' in op:
            op = op.replace('m', '')
        calc = str(entrada[:-2])
    else:
        op = entrada[-1]
        if 'm' in op:
            op = op.replace('m', '')
        calc = str(entrada[:-1])
    if "m" in entrada:
        redondo = int(input('Quantas casas decimais você deseja arredondar o resultado (0, 1 ou 2)? '))
        calc = float(calc)
        if redondo == 0:
            calc = ('%.0f' % calc)
        if redondo == 1:
            calc = ('%.1f' % calc)
        if redondo == 2:
            calc = ('%.2f' % calc)
        internop = str(input('Agora, digite um operador: '))
    fita.append(calc)
    if op == '':
        fita.append(internop)
    if op != '=':
        fita.append(op)
    if op == '=':
        break
    else:
        pass


fitastring = ' '.join([str(item) for item in fita])
resultado = Calculadora(fitastring)
result['Resultado'] = resultado.result

print(fita)
print(result)