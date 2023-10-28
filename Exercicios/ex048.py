soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma += c
print('A soma total de todos os {} valores é {}'.format(cont, soma))
