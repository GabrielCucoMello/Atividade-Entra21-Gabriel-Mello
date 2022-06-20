frase = str(input('Digite uma palavra ou frase:')).strip().upper()
print(frase)
print(type(frase))

# palavras = frase.split(sep=';') // Aqui inserimos um exemplo de separador por ; 

palavras = frase.split(sep=';')
print(palavras)
print(type(palavras))