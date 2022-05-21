aluno = [{
    'Nome': 'Gabriel',
    'Notas': [7.3,9.3,8.5,8.1]
}]

for media in aluno:
        print(f"Aluno --> {media['Nome']}")
        print(f"Notas --> {media['Notas']}")
        soma = sum(media['Notas'])
        print(f'Soma --> {soma}')
        qtdi = len(media['Notas'])
        print(f'Itens -> {qtdi}')
        media = soma / qtdi
        print(f'Media -> {media}')
        media_arredondada = round(media,1)
        print(f'Media arredondada --> {media_arredondada}')


boletim = []
boletim.append({'Nome': media['Nome'], 'Media das notas': media_arredondada})
print(boletim)

# deu errado sei la pq mas to com mt sono pra ir atrás