def leiaInt(txt):
    while True:
        try:
            num = int(input(txt).strip())
        except (ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return num


def linha(tam=42):
    print('-'*tam)


def doubleline(tam=42):
    print('='*tam)


def cabecalho(txt):
    doubleline()
    print(f'{txt:^42}')
    doubleline()


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    linha()
    opc = leiaInt('Sua opção: ')
    return opc