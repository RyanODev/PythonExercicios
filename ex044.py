print('{:=^40}'.format(' LOJAS GUANABARA '))
PC = float(input('Preço das Compras: R$'))
print('''Formas de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Escolha uma das opções acima: '))

if opcao == 1:
    valor = PC - (PC * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} com 10% de desconto.'.format(PC, valor))
elif opcao == 2:
    valor = PC - (PC * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} com 5% de desconto.'.format(PC, valor))
elif opcao == 3:
    print('Sua compra de {:.2f} será parcelada em 2x de {:.2f} SEM JUROS.'.format(PC, PC / 2))
elif opcao == 4:
    parcelas = int(input('Serão quantas parcelas? '))
    juros = (PC * 20 / 100)
    parcelacomjuros = (PC + juros) / parcelas
    print('Sua compra de R${:.2f} será parcelada em {}x de R${:.2f} COM JUROS'.format(PC, parcelas, parcelacomjuros))
    print('Sua compra de R${:.2f} no final custará R${:.2f}'.format(PC, PC + juros))
else:
    print('''\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO!
Tente Novamente.''')
