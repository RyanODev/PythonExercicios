# Minha Forma de resolver o desafio!
'''lista = [[], [], []]
dado = 0
for c in range(0, 9):
    dado = int(input('Digite um número: '))
    if len(lista[0]) <= 2:
        lista[0].append(dado)
    else:
        if len(lista[1]) <= 2:
            lista[1].append(dado)
        else:
            lista[2].append(dado)
print(lista[0])
print(lista[1])
print(lista[2])'''

# Forma do Guanabara!

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l], [c]}: '))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()