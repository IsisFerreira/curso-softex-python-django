''' Exercício 17: Sequência de Fibonacci
● Peça um número n ao usuário.
● Use um while para gerar e imprimir os primeiros n termos da sequência de Fibonacci (0,
1, 1, 2, 3, 5, ...).'''

n = int(input('\ndigite o número de termos da sequência de Fibonacci que você deseja gerar: \n'))

t1, t2 = 0, 1
cont = 0

if n <= 0:
   print('por favor, digite um número inteiro positivo.')
elif n == 1:
   print(f'a sequência de Fibonacci com {n} termo é:')
   print(t1)
else:
   print(f'os primeiros {n} termos da sequência de Fibonacci são:')
   while cont < n:
       print(f'termo n°{cont+1}: {t1}\n')
       proximo_termo = t1 + t2
       t1 = t2
       t2 = proximo_termo
       cont += 1
