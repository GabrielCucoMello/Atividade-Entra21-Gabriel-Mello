frase = str(input('Digite uma palavra ou frase:')).strip().upper()
# print(frase)
# print(type(frase))

# palavras = frase.split(sep=';') // Aqui inserimos um exemplo de separador por ; 

palavras = frase.split()
# print(palavras)
# print(type(palavras))

caracteres = ''.join(palavras)
# print(caracteres)
# print(type(caracteres))

tamanho = (len(caracteres))
# print(tamanho)

""" 
ex.:
rua dez
6 caracteres
   RUADEZ
 -10123456
 """


fraseinvertida = ''
for i in range((tamanho-1),-1,-1):
    # print(caracteres[i],end=' ')
    # fraseinvertida = fraseinvertida + caracteres[i]
    fraseinvertida += caracteres[i]
    
    # print(fraseinvertida,end=' ')
    
    # fraseinvertida += caracteres[i]
    # print(f'{i} Cr: {caracteres[i]}')

# range(start,stop,setep)
# range(inicio, fim, passo)

# for i in range(10,0,-1):
#     print(i,end=' ')

# print('\n')

# print(caracteres,fraseinvertida)

if fraseinvertida == caracteres:
    print('É um palindromo!!!')
else:
    print('não é')