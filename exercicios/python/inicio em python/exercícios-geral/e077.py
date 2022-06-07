def tam_frase():
    if len(frase1) > len(frase2):
        print(frase1)
    if len(frase1) < len(frase2):
        print(frase2)
    if len(frase1) == len(frase2):
        print(frase1, frase2)

frase1 = str(input('Digite a primeira frase: '))
frase2 = str(input('Digite a segunda frase: '))

x = tam_frase()
