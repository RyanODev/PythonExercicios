from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 4):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    elif idade < 18:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
