import pandas as pd

colunas = list(['Id', 'Nome', 'Idade', 'Sexo', 'Altura'])

class Pessoa():
    def __init__(self, pessoa):
        self.nome = pessoa.get('Nome')
        self.idade = pessoa.get('Idade')
        self.sexo = pessoa.get('Sexo')
        self.altura = pessoa.get('Altura')
    def hello(self):
        return f'Oi eu sou o {self.nome}, tenho {self.idade} anos, sou do sexo {self.sexo}, tenho {self.altura} metros'


class SheetReader():
    def __init__(self):
        self.content = {}

    def importa_planilha(self, sheet, colunas):
        df = pd.read_csv(sheet, index_col=0, header=0, usecols=colunas)
        return df.to_dict('index')

    def ler_planilha(self, df):
        for key, value in df.items():
            self.content[str(key)] = Pessoa(value)
    

ler = SheetReader()
ler.ler_planilha(
    ler.importa_planilha(
    sheet='https://docs.google.com/spreadsheets/d/e/2PACX-1vRVP_9oqZEMOa7vxxt4f7ME6ZXZ1VmPtbk5cHUuHCtSQ7p0Q5JanrwyczIY5ciRd3fmtguHL5uPcSsc/pub?output=csv',
    colunas = colunas)
    )

pessoa1 = ler.content.get('1')
print(pessoa1.hello())

pessoa2 = ler.content.get('2')
print(pessoa2.hello())

pessoa3 = ler.content.get('3')
print(pessoa3.hello())

