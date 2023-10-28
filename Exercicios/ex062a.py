termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 0
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        cont += 1
        termo += razao
        print(termo)
    mais = int(input('Quantos termos você quer mostrar? '))
print('A prgressão foi finalizada com {} termos'.format(total))