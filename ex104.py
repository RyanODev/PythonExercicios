def leiaInt():
    while True:
        num = input('Digite um número: ')
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO VÁLIDO.\033[m')
            

n = leiaInt()
print(f'O número que você digitou foi: {n}')