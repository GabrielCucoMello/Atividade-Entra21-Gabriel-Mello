import math


class Romano():
    def __init__(self, romanDict):
        self.romanDict = romanDict

    @classmethod
    def inteiroRomano(cls, A):
        cls.romanDict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }

        div = 1
        while A >= div:
            div *= 10
        
        div /= 10

        resultado = ""

        while A:
            lastNum = int(A / div)

            if lastNum <= 3:
                resultado += (cls.romanDict[div] * lastNum)
            elif lastNum == 4:
                resultado += (cls.romanDict[div] + cls.romanDict[div * 5])
            elif 5 <= lastNum <= 8:
                resultado += (cls.romanDict[div * 5] + (cls.romanDict[div] * (lastNum - 5)))
            elif lastNum == 9:
                resultado += (cls.romanDict[div] + cls.romanDict[div * 10])
            
            A = math.floor(A % div)
            div /= 10
        
        return resultado

valor = int(input('Digite um valor: '))
saida = Romano.inteiroRomano(valor)
print(saida)