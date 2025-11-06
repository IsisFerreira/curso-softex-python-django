vendas = [('Teclado', 50, 2), ('Mouse', 25.50, 4), ('Monitor', 300, 1), ('Fone', 45, 1), ('webcam', 75.20, 2)]
vendas_acimade100 = list() # []
produtos_unicos = set()

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        vendas_acimade100.append((produto, valor, quantidade))

    produtos_unicos.add(produto)

print(f'\nVendas acima de 100 reais: {vendas_acimade100}')        
print(f'\nprodutos únicos: {produtos_unicos}')  