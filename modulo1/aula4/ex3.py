'''Exercício 9: Somando Elementos de uma Lista
1. Crie uma lista de números.
2. Crie uma variável chamada soma e defina seu valor inicial como 0.
3. Use um loop for para percorrer cada número na lista.
4. Dentro do loop, adicione o valor do número atual à variável soma.
5. Após o loop, exiba o valor final da soma.'''

lista = [1,4,2,7,5,9]
soma = 0

for num in lista:
    soma += num
    
'''soma = sum(lista)'''
print(f'a soma da {lista} é {soma}')
