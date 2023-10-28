n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n == 999:
        break
    elif n != 999:
        soma += n
        cont += 1
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))
