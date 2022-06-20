class Biblioteca():
    def __init__(self, titulos):
        self.titulos = titulos
        

livros = Biblioteca()
livros.titulos = []

for i in range(int(input('Digite um número de titulos a serem adicionados: '))):
   livros.titulos = input(f"Entre o nome do livro {i + 1} para adicionar: ")
   print(f"Livro {livros.titulos} adicionado.")

print(livros.titulos)