def terreno(largura, comprimento):
    total = comprimento * largura
    print(f'\nA área de um terreno de {largura}x{comprimento} é de {total}m²')


print(f'{"Controle de Terreno":^30}')
print('='*30)
comp = float(input('COMPRIMENTO (m²): '))
larg = float(input('LARGURA (m²): '))
terreno(comp, larg)