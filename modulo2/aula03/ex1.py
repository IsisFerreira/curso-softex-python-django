class Motor:
    def ligar_motor(self):
        print(f'O carro está ligado.')

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        print('o motor está ligando')
        self.motor.ligar_motor() 

carro = Carro()

Carro.ligar()