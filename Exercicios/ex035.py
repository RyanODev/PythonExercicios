print('-=-' * 20)
print('\033[1;31mAnalisador de Triângulos\033[m')
print('-=-' * 20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + 3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;30;42mOS SEGUIMENTOS ACIMA PODEM FORMAR UM TRIÂNGULO!\033[m')
else:
    print('\033[1;30;41mOS SEGUIMENTOS ACIMA NÃO PODEM FORMAR UM TRIÂNGULO!\033[m')