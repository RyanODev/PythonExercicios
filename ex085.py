dados = [[], []]
for c in range(1, 6):
    dado = int(input(f'Digite o {c}º número: '))
    if dado % 2 == 0:
        dados[0].append(dado)
    else:
        dados[1].append(dado)
print(f'Os valores Pares são: {sorted(dados[0])}')
print(f'Os valores Ímpares são: {sorted(dados[1])}')