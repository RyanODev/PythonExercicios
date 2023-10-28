from time import sleep
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
print('Processando...')
sleep(1)
if resultado == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))
