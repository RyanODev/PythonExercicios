num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        print('Valor adicionado com sucesso!')
        num.append(n)
    else:
        print('Já tem esse número na lista >:(')
    r = ' '
    while r not in 'SN':
        r = str(input('Você deseja continuar?[S/N]')).upper().strip()[0]
    if r == 'N':
        break
print(sorted(num))