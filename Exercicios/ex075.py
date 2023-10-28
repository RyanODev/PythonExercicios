cont9 = i = pares = 0
numeros = (int(input('digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')))
print(f'Os números pares são: ', end='')
for c in numeros:
    if c == 9:
        cont9 += 1
    if c == 3:
        i = numeros.index(3)
    if c % 2 == 0:
        pares = c
        print(pares, end=' ')
print(f'\nO número 9 apareceu {cont9} vezes')
print(f'O número 3 apareceu pela primeira vez na posição {i}')
