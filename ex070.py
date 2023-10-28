total = contMil = cont = menor = 0
barato = ''
print('=' * 30)
print('{:^30}'.format('Lojas Guanabara'))
print('=' * 30)
while True:
    n = next = ' '
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    while next not in 'SN':
        next = str(input('Voce quer continuar?[S/N]')).upper().strip()[0]
    print('-' * 30)
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if preco >= 1000:
        contMil += 1
    if next == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'Foram {cont} produtos e o valor total foi = R${total:.2f}')
print(f'Foram {contMil} produtos que custam mais de R$1000.00')
print(f'O/A {barato} foi o produto com menor valor, custando: R${menor:.2f}')
