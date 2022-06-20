aluno = [{
    'Nome': 'Gabriel',
    'Notas': [7.3,9.3,8.5,8.1]
}]

print('Fase1:-----------')
print(aluno)

def calcula_media(aluno):
    print('Fase2:-----------')
    boletim = []
    for media in aluno:
        print(f"Aluno --> {media['Nome']}")
        if len(media['Notas']) > 0:
            temp = round(sum(media['Notas'])/len(media['Notas']),4)
            print(f"Notas: {media['Notas']}")
        else:
            temp = 0
        boletim.append({'Nome':media['Nome'], 'Media das notas': temp})
    print(boletim)

media_estudante = calcula_media(aluno)
print('Fase3:-----------')
print(aluno)