class FormaGeometrica:
    def __init__(self, cor):
        self.cor = cor

    def calular_area(FormaGeometrica):
        pass

class Retangulo(FormaGeometrica):

    def __init__(self, cor, largura, altura):
        super().__init__(cor, largura, altura)
        self._largura = largura
        self._altura = altura
    
    def calular_area(self):
        area = self._largura * self._altura 
        return area
    @property
    def largura(self):
        print("property foi chamado")
        return self._largura
    @property
    def altura(self):
        print("property foi chamado")
        return self._altura
    
class Quadrado(FormaGeometrica):
    def __init__(self, cor, lado):
        super().__init__(cor, lado)
        self._lado = lado
    
    def calular_area(self):
        area = self._lado**2
        return area
    @property
    def lado(self):
        print("property foi chamado")
        return self._lado

retangulo = Retangulo(10 ,5)
quadrado = Quadrado(5)

retangulo.calular_area()
quadrado.calular_area()
