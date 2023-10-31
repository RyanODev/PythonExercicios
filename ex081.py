lista = []
print('='*30)
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print('='*30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('Temos o valor 5 na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')