from random import randint

lista = []


def geravalores(list):
    print('Sorteando 5 valores dentro da lista: ', end='')
    for c in range(0, 5):
        list.append(randint(0, 10))
    for n in list:
        print(n, end=' ')


def somar(list):
    soma = 0
    for valor in list:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {list}, temos {soma}')


geravalores(lista)
somar(lista)