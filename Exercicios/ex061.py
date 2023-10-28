print('-=-' * 10)
print('Gerador de PA...')
print('-=-' * 10)

primeiro = int(input('Primeiro termo: '))
r = int(input('Qual a razão?: '))
cont = 1
termo = primeiro

while cont <= 10:
    print('{} ➞ '.format(termo), end='')
    termo += r
    cont += 1
print('Acabou!')
