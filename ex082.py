pares = []
impares = []
print('='*30)
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
    continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('='*30)
print(f'A lista completa é: {sorted(pares+impares)}')
print(f'A lista dos pares é: {pares}')
print(f'A lista dos ímpares é: {impares}')