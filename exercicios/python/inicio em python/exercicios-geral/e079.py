menor_20 = [' ', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = [' ', ' ', 'vinte', 'trinta', 'quarenta',
           'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
try:
    numero = int(input('Digite um número para ser transcrito em extenso: '))
except ValueError:
    print('Valor digitado não é um número')
try:
    if numero == 100:
        print('cem')

    elif numero == 0:
        print('zero')

    else:
        if numero < 20:
            print(menor_20[numero])
            numero = 0

        elif numero >= 20:
            print(dezenas[int(str(numero)[0])], end=' ')
            numero = numero - int(str(numero)[0])*10
        if numero != 0:
            print('e', menor_20[numero])
except IndexError:
    print('Número digitado não está dentre 1 e 100, tente novamente e digite outro dentro do limite.')
