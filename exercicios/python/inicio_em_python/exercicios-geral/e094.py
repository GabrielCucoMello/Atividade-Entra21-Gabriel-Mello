class Frase:
    def frasein(self):
        self.frase = str(input('Digite uma frase qualquer: '))

    def fraseup(self):
        self.frase = self.frase.upper()

    def fraseout(self):
        return self.frase
        


frases = Frase()
frases.frasein()
frases.fraseup()
print(frases.fraseout())