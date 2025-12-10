#Exercício 1, 2 , 3

"""class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
        
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

pessoa1.apresentar()
pessoa2.apresentar()"""

#Exercícico 4

"""class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Caderno", 15.50)
produto2 = Produto("Caneta", 3.00)

print(f"Produto: {produto1.nome}, Preço: R$ {produto1.preco}")
print(f"Produto: {produto2.nome}, Preço: R$ {produto2.preco}")"""

#Exercício 5

"""class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

conta = ContaBancaria("Ana", 100.00)

conta.depositar(50.75)

print(f"Saldo atual da conta de {conta.titular}: R$ {conta.saldo}")""" 

#Exercício 6
"""class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado.".format(valor))
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            print("Saldo insuficiente.")
    
    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")


conta = ContaBancaria("Carlos", 200.00)

conta.mostrar_saldo()        

conta.sacar(100.00)          
conta.mostrar_saldo()       

conta.sacar(150.00)          
conta.mostrar_saldo()   """    

#Exercício 7

"""class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

ret = Retangulo(5, 3)

print(f"Área do retângulo: {ret.calcular_area()}")          
print(f"Perímetro do retângulo: {ret.calcular_perimetro()}") """

#Exercício 8
"""
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0  
    
    def abastecer(self, litros):
        if litros > 0:
            self.nivel_combustivel += litros
            print(f"Abastecido {litros} litros. Nível atual: {self.nivel_combustivel} L")
        else:
            print("Quantidade inválida para abastecimento.")
    
    def dirigir(self, distancia):
        consumo_necessario = distancia / 10  
        
        if self.nivel_combustivel >= consumo_necessario:
            self.nivel_combustivel -= consumo_necessario
            print(f"O carro {self.modelo} percorreu {distancia} km.")
            print(f"Combustível restante: {self.nivel_combustivel:.2f} L")
        else:
            print(f"Combustível insuficiente para percorrer {distancia} km.")
            print(f"Faltam {consumo_necessario - self.nivel_combustivel:.2f} litros.")


meu_carro = Carro("Fusca 1976")

meu_carro.abastecer(40)      
meu_carro.dirigir(150)        
meu_carro.dirigir(300)        
meu_carro.dirigir(100)         """

#Exercício 9

"""class Funcionario:
    percentual_bonus = 1.10
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus

func1 = Funcionario("Ana", 4000.00)
func2 = Funcionario("Pedro", 5200.00)

print(f"Salário {func1.nome}: R$ {func1.salario}")
print(f"Salário {func2.nome}: R$ {func2.salario}")

func1.aplicar_bonus()
func2.aplicar_bonus()

print(f"Novo salário {func1.nome}: R$ {func1.salario}")
print(f"Novo salário {func2.nome}: R$ {func2.salario}")"""

#Exercício 10

"""class Motor:
    def __init__(self, potencial):
        self.potencial = potencial

class Carro:
    def __init__(self, modelo, potencial_motor):
        self.modelo = modelo
        self.motor = Motor(potencial_motor)
    
    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem motor com {self.motor.potencial} cavalos de potência.")

carro1 = Carro("Civic", 150)
carro2 = Carro("Corolla", 140)"""

#Exercício 11

"""class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []
    
    def adicionar_livro(self, livro):
        self.acervo.append(livro)
    
    def listar_livros(self):
        if not self.acervo:
            print("A biblioteca está vazia.")
        else:
            print("Livros na biblioteca:")
            for livro in self.acervo:
                print(f"- {livro.titulo}, de {livro.autor}")

biblioteca = Biblioteca()

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()"""

#Exercício 12

"""class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
    
    def __str__(self):
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"

filme1 = Filme("De Volta para o Futuro", "Robert Zemeckis", 1985)
filme2 = Filme("Interestelar", "Christopher Nolan", 2014)

print(filme1)
print(filme2)"""