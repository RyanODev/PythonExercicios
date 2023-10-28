v = int(input('Qual a velocidade que você está percorrendo? '))
multa = (v - 80) * 7
if v > 80:
    print('Multado. Reduza a velocidade!')
    print('Sua multa é de {} reais'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
