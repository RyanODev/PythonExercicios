listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caneta', 2.50, 'Estojo', 6.80, 'Bolsa',
            135.90, 'Caderno', 15.50, 'Lapiseira', 7.75, 'Grafite', 3.50, 'Corretivo', 5, 'Pasta', 6.99)
print('='*40)
print(f'{"Listagem de Materiais":^40}')
print('='*40)
for itens in range(0, len(listagem)):
    if itens % 2 == 0:
        print(f'{listagem[itens]:.<30}', end='')
    else:
        print(f'R${listagem[itens]:>7.2f}')
print('='*40)