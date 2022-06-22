num = int(input('Digite um número para verificar se ele é perfeito: '))
cont = 1
soma = 0

while (cont < num): # Loop que ocorre enquanto o contador é menor do que n
    if (num % cont) == 0: # Divide o numero pelo contador, se o resto for 0, ele é divisor
        soma = soma + cont # Adiciona o contador constado como divisor à variável soma
        cont = cont + 1 # Incrementa mais um ao contador para continuar o loop
    else:
        cont = cont + 1 # Caso não for divisor, ele apenas acrescenta ao contador
    
if (soma == num): # Verifica se a soma dos divisores é o mesmo do que o numero digitado
    print(f'O número {num} é perfeito!')
else:
    print(f'O número {num} não é perfeito.')

