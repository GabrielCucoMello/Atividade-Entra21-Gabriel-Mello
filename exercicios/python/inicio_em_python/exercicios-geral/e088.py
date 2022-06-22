def quadrado(num):
    '''
    Aqui, pegamos o numéro (num) dado como input pelo usuário 
    e o elevamos ao quadrado, retornando apenas o resultado.
    num = inteiro
    '''
    return num ** 2

try:
    num = int(input('Digite um número inteiro: '))
    print(quadrado(num))
except:
    print('Conteúdo digitado não é um número inteiro.')