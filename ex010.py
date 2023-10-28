a = float(input('Quanto você tem na carteira? R$'))
d = a / 4.87
i = a * 30.36
e = a / 5.20
print('Com R${:.2f} que você tem na carteira, pode-se comprar: \nUS${:.2f} dólares \n€{:.2f} euros \n¥{:.2f} ienes'.format(a, d, e, i))

