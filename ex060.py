from time import sleep
'''num = int(input('Digite um número para
calcular o seu fatorial: '))

c = num
f = 1

print('Calculando... {}! '.format(c))
sleep(1.5)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    sleep(0.5)
    print(f)
'''

n = int(input('Digite um número: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    sleep(0.5)
print(f)
