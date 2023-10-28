s = float(input('Digite o Valor do salário: R$'))
a = 15 / 100 * s    # pra dar aumento você, primeiro divide e depois multiplica!
sa = s + a
print('O aumento é de: {:.2f} '.format(a))
print('O salário com aumento fica: {:.2f}'.format(sa))
