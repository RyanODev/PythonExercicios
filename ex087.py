matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insira um número na posição {[l], [c]}: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        # final dos pares


print('='*40)

print(f'A soma dos valores pares é igual a {par}.')
# ======================================================
for l in range(0, 3):
    soma += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma}')
# ======================================================
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda coluna é {maior}')
# =======================================================
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
