acesso = [
            ('Pedro', 'sucesso'), 
            ('Ana', 'falha'),
            ('Maria', 'sucesso'),
            ('Pedro', 'falha'),
            ('Ana', 'falha')
            ]

nome_sucesso = set()
nome_falha = set()

for nome, status in acesso:
    if status == 'sucesso' :
        nome_sucesso.add(nome)
    elif status == 'falha':
        nome_falha.add(nome)

nome_falha = nome_falha.difference(nome_sucesso)

print(f'\nnome das pessoas com login bem sucedidos: {nome_sucesso}')
print(f'\nnome das pessoas com login com falhas: {nome_falha}')