'''Exercício 14: Somador de Números Positivos
● Use um while True para pedir números ao usuário.
● Some todos os números positivos.
● Se o usuário digitar um número negativo, use break para sair do loop e imprima a soma'''
total = 0
while True:
    x = int(input('me de numeros: \n'))
    if x > 0:
        total =+ x
    else:
        print(f'a soma dos numeros positivos inseridos é {total}')
        break

