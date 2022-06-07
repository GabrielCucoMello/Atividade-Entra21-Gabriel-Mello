class Calculadora():
    
    def soma(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mult(self, num1, num2):
        return num1 * num2
    
    def div(self, num1, num2):
        return num1 / num2


contas = Calculadora()

print('1 -> Soma')
print('2 -> Subtração')
print('3 -> Multiplicação')
print('4 -> Divisão')
conta = int(input('Digite o número de qual tipo de operação você deseja fazer: '))

if conta == 1:
    print(contas.soma(int(input('Digite o primeiro número: ')), int(input('Digite um segundo número: '))))

if conta == 2:
    print(contas.sub(int(input('Digite o primeiro número: ')), int(input('Digite um segundo número: '))))

if conta == 3:
    print(contas.mult(int(input('Digite o primeiro número: ')), int(input('Digite um segundo número: '))))

if conta == 4:
    print(contas.div(int(input('Digite o primeiro número: ')), int(input('Digite um segundo número: '))))

if conta != 1 and conta != 2 and conta != 3 and conta != 4:
    print('Você não digitou nenhuma opção válida.')