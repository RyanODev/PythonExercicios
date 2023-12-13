from time import sleep


def maior(*num):
    cont = nmaior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.5)
        if cont == 0:
            nmaior = n
        else:
            if n > nmaior:
                nmaior = n
        cont += 1
    print(f'Foram passados {len(num)} valores')
    print(f'O maior valor informado foi: {nmaior}')


maior(4, 331, 5, 255, 2, 7, 10)
maior(4, 5, 255, 2, 7, 10)
maior(1, 0, 3, -1)