num = int(input("Digite um número para ser convertido: "))
print('''Escolha uma das bases para conversão:
Digite [ 1 ] para binário
Digite [ 2 ] para Octal
Digite [ 3 ] para Hexadecimal''')
base = int(input('Escolha sua opção '))

if base == 1:
    print('A conversão de {} para base binária é {}'.format(num, bin(num) [2:]))
elif base == 2:
    print('A conversão do número {} para base octal é {}'.format(num, oct(num) [2]))
elif base == 3:
    print('A conversão do número {} para base hexadecimal é {}'.format(num, hex(num) [2:]))
else:
    print('\033[31mOpção inválida! Tente novamente.')