import random


class GeradorDeAtracoesSetor():
    def __init__(self):
        self.setor = []
        self.atracoes = ['RODA GIGANTE', 'MONTANHA RUSSA', 'MONTANHA RUSSA AO CONTRARIO', 'SHOW DE MANOBRAS', 'KART', 'GIGA TOWER', 'TOBOAGUA','CARROSSEL', 
    'SHOW GALINHA PINTADINHA', 'BARCO VIKING', 'CARRINHO BATE BATE', 'PEDALINHO', 'SHOW PATRULHA CANINA', 'ESPAÇO KIDS', 'LIMPEZA', 'PRAÇA DE ALIMENTAÇÃO', 'PORTARIA', 'SEGURANÇA']
    
    def GeraAtracoes(self):
        contador = 0
        while contador < len(self.atracoes):
            letra = chr(random.randint(ord('A'), ord('G')))
            num = random.randint(1, 6)
            letra_num = f'{letra}{num}'
            self.setor.append(letra_num)
            contador += 1