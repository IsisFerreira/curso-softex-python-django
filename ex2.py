class GraodeCafe:
    def __init__(self):
        pass

    def moer(self):
        print('Os graos de café foram moidos.')

class Agua:
    def __init__(self):
        pass

    def aquecer(self):
        print("A agua está quente")

class Cafeteira:
    def __init__(self):
        self.agua = Agua
        self.graodecafe = GraodeCafe

    def prepararCafe(self):
        self.graodecafe.moer()
        self.agua.aquecer()
        print('seu café ta pronto')

cafe = Cafeteira()

cafe.prepararCafe()