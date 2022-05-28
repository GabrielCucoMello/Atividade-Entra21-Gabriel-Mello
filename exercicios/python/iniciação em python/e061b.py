def itself(n):
    print('N:', n)
    if n <= 1:
        return n
    else:
        ret = itself(n-1) + itself(n-2)
        return ret


num = int(input('Digite um número: '))
x = itself(num-1)
print('Fim: ', x)
