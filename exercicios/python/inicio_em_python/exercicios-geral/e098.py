try:
    nota = float(input('Digite a nota do aluno, em um valor entre 0.0 e 1.0: '))
    if nota >= 0.6 and nota <= 1.0:
        print('Aluno aprovado!')
    if nota < 0.6:
        print('Aluno em situação de recuperação!')
    if nota >= 1.1:
        print('Digite apenas uma nota dentro dos limites dados!')
        quit()
except ValueError:
    print('Você não digitou um número')
    quit()