from random import randint
'''cont = menor = maior = 0'''
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
numeros = n
print(f'Lista de números: {n}')
'''for c in n:
    if cont == 0:
        menor = n[cont]
        maior = n[cont]
    else:
        if n[cont] > maior:
            maior = n[cont]
        if n[cont] < menor:
            menor = n[cont]
    cont += 1'''
print(f'O menor número foi: {max(numeros)}')   # usando o max e o min corta esse código de cima inteiro
print(f'E o maior número foi: {min(numeros)}')
