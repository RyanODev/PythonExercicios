from datetime import date
ano = int(input('Que ano você quer analizar? Escreva 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # se ano resto 4 for igual a 0 e ano resto 100 for diferente de 0 ou então o ano ser divisível por 400
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))