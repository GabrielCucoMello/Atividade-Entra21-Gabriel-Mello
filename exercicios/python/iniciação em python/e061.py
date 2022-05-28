def fibonnacci(n):
    if n <= 1:
        return n
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

num = int(input('Digite um número para encontrar seu Fibonacci: '))

resposta = fibonnacci(num-1)
print(resposta)