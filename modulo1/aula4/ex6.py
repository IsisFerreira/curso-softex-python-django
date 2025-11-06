'''Exercício 12: Acumulador de Soma
● Peça ao usuário para digitar 5 números.
● Use um while com um contador para somar todos os números digitados e imprimir o
resultado final.'''
cont = 0
for i in range(5):
    x = int(input('\ninsira um numero inteiro: \n'))
    cont += x
print(cont)
