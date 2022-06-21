class Morse(object):
    def __init__(self):
        self.morse_dict = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-',
            'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--',
            'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
            '0': '-----'
        }

    def decodificar(self, codigo_morse):
        codigo = codigo_morse.split(' ')
        texto = ' '
        for item in codigo:
            for key, value in self.morse_dict.items():
                if item == value:
                    texto += key
                    break
        return texto

    def codificar(self, texto_plano):
        codigo = ' '
        for i in texto_plano.upper():
            if i in self.morse_dict.keys():
                codigo += self.morse_dict[i] + ' '
        return codigo


morse = Morse()

escolha = int(input(
    'Caso queira codificar um código morse, digite "1", caso queira decodificar, digite "2": '))

if escolha == 1:
    texto_in_cod = input('Digite um texto para ser convertido em Código Morse: ')
    codigo = morse.codificar(texto_in_cod)
    print('Codigo morse codificado: {0}'.format(codigo))

if escolha == 2:
    texto_in_dec = input('Digite um texto para ser decodificado de Código Morse: ')
    codigo_decod = morse.decodificar(texto_in_dec)
    print('Texto decodificado: {0}'.format(codigo_decod))
