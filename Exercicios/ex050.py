soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite O {}º valor: '.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        soma += c
print('A soma dos {} números equivalem a {}'.format(cont, soma))
