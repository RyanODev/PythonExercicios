a = float(input('Digite o valor do produto: R$'))
d = (a * 5 / 100)     # pra dar desconto, voce primeiro multiplica e depois divide!
vd = a - d
print('O desconto de 5% é de R${:.2f}: '.format(d))
print('O valor com desconto fica R${:.2f}'.format(vd))
