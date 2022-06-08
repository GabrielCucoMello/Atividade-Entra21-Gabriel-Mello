class Pessoa:
    def __init__(self, nome, login=False, logoff=False):
        self.nome = nome
        self.login = login
        self.logoff = logoff

    def logar(self):
        print(f'Seja bem vindo {self.nome}, você está logado no sistema!')
        self.login = True
    
usuario = Pessoa(str(input('Digite seu nome para efetuar o login: ')))
print(usuario.login)

usuario.logar()
print(usuario.login)