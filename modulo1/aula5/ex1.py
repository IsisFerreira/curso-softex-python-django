'''Exercício 13: Login com Tentativas
● Defina uma senha secreta.
● Use um while True e um contador de tentativas (máximo de 3).
● Se o usuário acertar a senha, imprima "Login bem-sucedido!" e use break.
● Se o usuário errar 3 vezes, imprima "Tentativas esgotadas!" e pare o programa.
'''

senha = 'senhasecreta123'
cont = 3

while cont > 0:
    cont -= 1
    tentativa = input('digite seu palpite: \n')
    print(f'tentativa restantes: {cont}')
    if tentativa == 'senhasecreta123':
        print('parabéns, você venceu! \n')
    else: 
        print('você perdeu!!! ')
