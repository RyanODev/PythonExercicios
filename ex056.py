media = 0
maisvelho = 0
maisvelha = 0
a = ''
b = ''
contadorM = 0
contadorF = 0
for pessoas in range(1, 6):
    print('----- {}ª pessoa -----'.format(pessoas))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper()
    media += idade / 5
    if sexo == 'M':
        if pessoas == 1:
            maisvelho = idade
            a = nome
        else:
            if maisvelho < idade:
                maisvelho = idade
                a = nome
        contadorM += 1
    elif sexo == 'F':
        if pessoas == 1:
            maisvelha = idade
            b = nome
        else:
            if maisvelha < idade:
                maisvelha = idade
                b = nome
        contadorF += 1
print('A média de idade desse grupo é de {} anos'.format(media))
print('A idade do homem mais velho é {} anos e se chama {}'.format(maisvelho, a))
print('A idade da mulher mais velha é {} anos e se chama {}'.format(maisvelha, b))
print('Ao todo são {} mulheres e {} homens'.format(contadorF, contadorM))
