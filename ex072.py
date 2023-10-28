numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Escolha um número de 1 a 10: '))
    if 0 < num <= 20:
        break
print('Você digitou o número:', numeros[num])
print('-' * 30)
