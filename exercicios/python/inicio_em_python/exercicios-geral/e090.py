try:
    num = input('Digite alguns números separados por vírgula: ').strip()
    numeros = [int(val) for val in num.split(',')]

    print('Aqui estão os números digitados sortidos: ')
    print(sorted(numeros))

except:
    print('Você digitou um caractere que não é válido, tente novamente usando apenas números separados por ","')