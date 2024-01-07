def leiaInt():
    while True:
        try:
            num = int(input('Digite um número Inteiro: ').strip)
        except:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        else:
            return num


def leiaFloat():
    while True:
        try:
            num = float(input('Digite um número Real: ').strip)
        except:
            print('\033[0;31mERRO! DIGITE UM NÚMERO REAL VÁLIDO.\033[m')
        else:
            return num


a = leiaInt()
b = leiaFloat()
print(f'Os números que você digitou foi: {a} e {b}')