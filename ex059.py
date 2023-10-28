from time import sleep
pvalor = int(input('Primeiro Valor: '))
svalor = int(input('Segundo Valor: '))

opcao = 0

while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>> Qual a sua opção? '))
    sleep(1)
    if opcao == 1:
        soma = pvalor + svalor
        print('A soma entre {} + {} é {}'.format(pvalor, svalor, soma))
        print('-==-' * 15)

    elif opcao == 2:
        multiplicacao = pvalor * svalor
        print('A multiplicacao entre {} e {} é {}'.format(pvalor, svalor, multiplicacao))
        print('-==-' * 15)

    elif opcao == 3:
        if pvalor > svalor:
            print('Entre {} e {} o maior é {}'.format(pvalor, svalor, pvalor))
            print('-==-' * 15)

        elif pvalor == svalor:
            print('Entre {} e {} não existe um maior valor!'.format(pvalor, svalor))

        else:
            print('Entre {} e {} o maior valor é {}'.format(pvalor, svalor, svalor))
            print('-==-' * 15)

    elif opcao == 4:
        print('Informe os números novamente...')
        pvalor = int(input('Primeiro Valor: '))
        svalor = int(input('Segundo Valor: '))
        print('-==-' * 15)

    elif opcao == 5:
        break

    else:
        print('Número inválido! Tente novamente.')
sleep(1.5)
print('Fim do programa. Volte sempre!')