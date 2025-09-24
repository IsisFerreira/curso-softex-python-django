class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def Apresentar(self):
        print(f"\nOlá, meu nome é {self.nome} e tenho {self.idade} anos")

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula ):
        super().__init__(nome, idade)
        self.matricula = matricula

    def Apresentar(self):
        print(f"\nOlá, meu nome é {self.nome} e tenho {self.idade} anos e minha matricula é {self.matricula}")

pessoa = Pessoa("Ana", "19")
estudante = Estudante("Ana", "19", "976806")

pessoa.Apresentar()
estudante.Apresentar()

lista_objetos:list[Pessoa] = [pessoa, estudante]

for objeto in lista_objetos:
    objeto.Apresentar()