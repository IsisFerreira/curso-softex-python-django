'''Exercício 8: Buscando uma Palavra em uma Frase
1. Peça ao usuário que digite uma frase e guarde-a em uma variável.
2. Peça ao usuário que digite uma palavra e guarde-a em outra variável.
3. Use o operador in dentro de uma estrutura if para verificar se a palavra está contida na
frase.
4. Exiba uma mensagem informando se a palavra foi encontrada ou não.
'''

frase = input('Digite uma frase: \n')
palavra = input('Digite uma palavra: \n')

if palavra in frase:
    print('Palavra encotrada!')
else:
    print('Palavra não encontrada!')
