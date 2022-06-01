from mimetypes import init


class Pessoa:
    administrador = 'Admin'

    def __init__(self, nome, msg):
        self.nome = nome
        self.msg = msg
        print('init:', msg)

    def metodo1(self):
        print('Met1:', self.msg)
        pass
