contM = tot18 = contF = 0

while True:
    print('-' * 20)
    print('Cadastre uma Pessoa')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo:[F/M] ')).upper().strip()
        if sexo == 'M':
            contM += 1
        if idade >= 18:
            tot18 += 1
        if sexo == 'F' and idade < 20:
            contF += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).upper().strip()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {contM} homens cadastrados')
print(f'E temos {contF} mulheres com menos de 20 anos.')