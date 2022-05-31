aluno = [{
    'Nome': 'Gabriel',
    'Notas': [7.3,9.3,8.5,8.1]
}]

def cm(aluno):
    boletim = []
    for media in aluno:
        mr = round(sum(media['Notas']) / len(media['Notas']), 1)
        boletim.append({'Nome': media['Nome'], 'Media das notas': mr})
    return boletim

bl = (cm(aluno))
print(bl)