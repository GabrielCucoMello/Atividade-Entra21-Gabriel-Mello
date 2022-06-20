base = {
    'Pergunta 1': {
        'pergunta':'Qual é o ano que estamos atualmente?',
        'alternativas':{
            'a':'2021',
            'b':'2022',
            'c':'1922',
            'd':'1833'
        },
        'respostac':'b'
    },
    'Pergunta 2 ':{
        'pergunta':'Qual é o ano que o SENNA morreu?',
        'alternativas':{
            'a':'1999',
            'b':'2001',
            'c':'1994',
            'd':'1989',
        },
        'respostac':'c'  
    }
}

respostas_certas = 0

#display de perguntas:
for numper, per in base.items(): #numper: indica em qual pergunta estamos, per: indica a pergunta feita
    print(f'{numper}:{per["pergunta"]}')
    #display de alternativas:
    for altlet, altres in per['alternativas'].items(): #altlet: letra da alternativa, altres: texto da alternativa
        print(f'[{altlet}]:{altres}')
    
    resposta = input('Escolha uma das alternativas: [a], [b], [c] ou [d] \n') #input para adicionar resposta por parte do user
    print('')
    if resposta == per['respostac']: #verificação de respostas
        print('Resposta exata!')
        respostas_certas += 1
    else:
        print('Resposta incorreta')

if respostas_certas == 0: #display de sumário das respostas com 0 acertos
    print('Você errou todas as questões.')
elif respostas_certas == 1: #display de sumário das respostas com 1 acerto
    print('Você acertou apenas uma questão.')
else: #display de sumário das respostas contabilizando todos os acertos
    print(f'Você acertou [{respostas_certas}] questões. Parabéns!')
