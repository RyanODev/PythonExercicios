def leiaInt():
    while True:
        try:
            num = int(input('Digite um número Inteiro: ').strip())
        except (ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return num


def leiaFloat():
    while True:
        try:
            num = float(input('Digite um número Real: ').strip())
        except ValueError:
            print('\033[0;31mERRO! DIGITE UM NÚMERO REAL VÁLIDO.\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            break
        else:
            return num


a = leiaInt()
b = leiaFloat()
print(f'Os números que você digitou foram: {a} e {b}')