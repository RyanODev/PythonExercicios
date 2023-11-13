# MINHA FORMA DE RESOLVER O DESAFIO!
"""from random import randint
from time import sleep
print('='*30)
print(f'{"Joga na mega sena":^30}'.upper())
print('='*30)
numeros = []
cont = 0
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('=-'*3, f"{f'Sorteando {jogos} jogos':^13}", '=-'*3)
sleep(1)
for n in range(1, jogos + 1):
    cont += 1
    numeros = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
    sleep(0.5)
    print(f'Jogo {cont}:', numeros)
"""
# PROPOSTA DO GUANABARA:


from random import randint
from time import sleep
lista = list()
cont = 0
jogos = []
tot = 1
print('='*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('='*30)
sleep(0.5)
quant = int(input('Quantos jogos você quer sortear? '))
print('-='*3, f'{f"Sorteando {quant} jogos":^18}', '=-'*3)
sleep(1)
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('='*35)
print(f'{"BOA SORTE!":^35}')
print('='*35)
