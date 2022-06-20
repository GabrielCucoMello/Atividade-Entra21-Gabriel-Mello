tudo = 0


class Global():
    def __init__(self):
        global tudo
        tudo = tudo + 2
        print(tudo)


class Local():
    def __init__(self):
        tudo = 3
        print(tudo + 1)


result1 = Global()
result2 = Local()

# nao se usa assim em classe, mas ta aí a adesão de conhecimento