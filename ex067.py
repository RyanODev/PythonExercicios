n = cont = mult = 0
while True:
    cont -= 10
    n = int(input('Você quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while cont != 10:
        cont += 1
        if cont == 10:
            break
        print(f'{n} x {cont} = {n*cont}')
    print('-=-' * 10)
print('Programa Tabuada Encerrado. Volte Sempre!')
