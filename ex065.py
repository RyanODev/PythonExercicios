n = cont = maior = menor = 0
continuar = 'S'

while continuar != 'N':
    cont += 1
    n = int(input('Digite uma Número: '))
    continuar = str(input('Quer continuar?[S/N]: ')).upper()
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = n / cont
print('você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior número que você digitou foi {} e o menor é  {}'.format(maior, menor))
