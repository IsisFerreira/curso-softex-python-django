'''Exercício 10: Contador Regressivo
● Peça um número inteiro ao usuário.
● Use um while para fazer uma contagem regressiva a partir desse número até 0. Imprima
cada número.
'''

x = int(input('insira um numero inteiro para uma contagem regressiva: \n'))

while x > 0:
    x -= 1
    print(x)

