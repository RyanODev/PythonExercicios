print('-=' * 20)
print('Gerador de PA...')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro

continuar = ''
total = 0
cont = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} ➞ '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa...', end='\n')
    mais = int(input('Quantos termos você quer mostrar? '))
print('Progressão finalizada com {} termos.'.format(total))
