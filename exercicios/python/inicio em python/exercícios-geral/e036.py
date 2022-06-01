frase = str(input('Digite uma palavra ou frase: ')).strip().upper()

palavras = frase.split()

caracteres = ''.join(palavras)
fraseinvertida = ''

for i in range(
    len(caracteres)-1,-1,-1):
    fraseinvertida += caracteres[i]

print(caracteres, fraseinvertida)

if fraseinvertida == caracteres:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')