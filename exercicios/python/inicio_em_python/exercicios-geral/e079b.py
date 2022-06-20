#exemplo do e079 utilizando a biblioteca num2words
from num2words import num2words

try:
    numero = int( input('Digite um número de 0 a 100 para ser transcrito em extenso: ') )
    extenso = num2words(numero, lang='pt-br')
    print(f'Número por extenso: {extenso}')
except ValueError:
    print('Você não digitou um número.')