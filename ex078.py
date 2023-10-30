lista = []
cont = 0
menor = maior = 0
for c in range(0, 6):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-=-'*20)
print(f'Você digitou os valores {lista}')
for v in lista:
    if cont == 0:
        maior = menor = v
    else:
        if maior < v:
            maior = v
        if menor > v:
            menor = v
    cont += 1
print(f'O menor valor digitado foi {menor} na posição: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()
print(f'O maior valor digitado foi {maior} na posição: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
