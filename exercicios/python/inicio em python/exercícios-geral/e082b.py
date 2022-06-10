tudo = 'global dentro da classe 2'

class Local():
    def __init__(self):
        self.tudo = 'local dentro da classe 1'

class Global():
    def __init__(self):
        global tudo
        self.tudo =tudo

result1 = Global()
print(result1.tudo)
result2 = Local()
print(result2.tudo)