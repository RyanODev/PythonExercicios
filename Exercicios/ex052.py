num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}\033[m'.format(c), end=' ')
print('\nO número \033[1;34m{}\033[m foi divisível \033[1;34m{}\033[m vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
