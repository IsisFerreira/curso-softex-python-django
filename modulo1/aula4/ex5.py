'''Exercício 11: Tabuada Simples
● Peça um número ao usuário.
● Use um while para imprimir a tabuada desse número, de 1 a 10.
○ Exemplo: 5 x 1 = 5, 5 x 2 = 10, etc'''

x = int(input('\ninsira um numero inteiro: \n'))
i = 0
while i < 10:
    i += 1
    print(f'{x} X {i} = {x*i}')
