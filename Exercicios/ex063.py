print('-'*25)
print('Sequência de Fribonacci')
print('-'*25)
n = int(input('Quantos números você quer mostrar? '))
t1 = 0
t2 = 1

cont = 1
print('~'*60)
while cont <= n:
    t3 = t1 + t2
    print(' {} ⇢'.format(t1), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' Acabou!')
print('~'*60)