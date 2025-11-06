'''Exercício 15: Validação de E-mail
● Use um while True para pedir um e-mail ao usuário.
● Verifique se o e-mail contém o caractere @.
● Se contiver, imprima "E-mail válido" e use break.
● Se não contiver, imprima "E-mail inválido. Digite novamente."'''

while True:
    email = input('\nQual seu email? \n')

    x = email.find('@')
    if x == -1:
        print('email inválido!\n')
        break
    else:
        print('email válido!\n')
