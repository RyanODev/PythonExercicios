def fatorial(num, show=False):
    """
    Fatorial(n, show=False)
    --> Calcula o fatorial de um número
    :param num: Número a ser calculado
    :param show: (OPCIONAL) mostrar ou não a conta
    :return: o valor fatorial de um número n
    """
    r = 1
    for c in range(num, 0, -1):
        r *= c
        if show == True:
            print(f'{c}', 'x' if c != 1 else '=', end=' ')
    return r


fator = int(input('Digite um número: '))
print(fatorial(fator))