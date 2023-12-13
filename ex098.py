from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i < f:
        for a in range(i, f, p):
            print(f'{a} ', end='')
            sleep(0.3)
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.3)
    print()


contador(0, 11, 1)
contador(10, 0, 2)
print('='*40)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))