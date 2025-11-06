notas = [
        ('Ana', 9.5),
        ('João', 8.0), 
        ('Maria', 10.0),
        ('Pedro', 7.5), 
        ('Ana', 10.0), 
        ('Carlos', 6.5)
        ]
maior_nota = 0
for _nota in notas:
    if nota > maior_nota:
        maior_nota = nota
print('\nmaior nota {maior_nota}')

alunos_maior_nota = []
for aluno, nota in notas:
    alunos_maior_nota.append(aluno)
alunos_maior_nota = tuple(alunos_maior_nota)
print(f'\nAlunos que tiraram a maio nota: {alunos_maior_nota}')

alunos_notas_baixas = {aluno for aluno in notas if nota < 7}