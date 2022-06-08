#exemplo do e079 utilizando a biblioteca num2words
from num2words import num2words

numero = int( input('Digite um número para ser transcrito em extenso: ') )
extenso = num2words(numero, lang='pt-br')

print(f'Número por extenso: {extenso}')