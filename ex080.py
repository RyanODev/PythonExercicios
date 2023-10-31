lista = []
cont = 0
print('='*35)
for c in range(0, 4):
    a = int(input('Digite um número: '))
    if c == 0 or a > lista[-1]:
        lista.append(a)
        print('Adicionado ao final da lista...')
    elif a < lista[0]:
        lista.insert(0, a)
        print('Adicionado ao começo da lista...')
    elif a > lista[0]:
        lista.insert(1, a)
        print('Adicionado no meio da lista...')
print('='*35)
print(f'Os valores foram: {lista}')
print('='*35)