casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto você ganha? R$'))
anos = int(input('Em quanto tempo você quer pagar? '))

prestacao = casa / (anos * 12)
trintaporcento = salario * 30 / 100

if prestacao > trintaporcento:
    print('\033[31m-=-' * 30)
    print("\033[31mSeu Empréstimo foi Negado!")
    print('\033[31mO valor da parcela excedeu 30% do seu salário')
    print('30% do salário = R${}'.format(trintaporcento))
    print('\033[31mValor da parcela = R${:.2f}'.format(prestacao))
    print('\033[31m-=-' * 30)
elif prestacao <= trintaporcento:
    print('\033[32m-=-' * 30)
    print('\033[32mSeu Empréstimo foi Aprovado!')
    print('\033[32mFicou {} parcelas no valor de R${:.2f}'.format(anos, prestacao))
    print('\033[32m-=-' * 30)