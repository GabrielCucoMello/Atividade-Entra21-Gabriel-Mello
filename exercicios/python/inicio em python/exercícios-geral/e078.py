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
            '0': '-----', ', ': '--..--', '.': '.-.-.-',
            '?': '..--..', '/': '-..-.', '-': '-....-',
            '(': '-.--.', ')': '-.--.-'
        }

    def codificar(self, texto_plano):
        codigo = ' '
        for i in texto_plano.upper():
            if i in self.morse_dict.keys():
                codigo += self.morse_dict[i] + ' '
        return codigo


texto = input('Digite um texto para ser convertido em Código Morse: ')

morse = Morse()
codigo = morse.codificar(texto)
print('Codigo morse: {0}'.format(codigo)) 
