jogador = {}
partidas = []
time = []
while True:
    print('-='*30)
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas[:])
    time.append(jogador.copy())
    resp = ' '
    while resp not in "SN":
        resp = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-'*30)
print(f'{"Nº  "}', end='')
for i in jogador.keys():
    print(f'{i:<18}', end='')
print()
print('-'*60)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Você quer mostrar os dados de qual jogador?[999 para] '))
    if busca == 999:
        break
    if busca > len(time):
        print('NÚMERO INVÁLIDO! TENTE NOVAMENTE.')
    else:
        print(f' --Levantamesto de dados do jogador {time[busca]["Nome"]}--')
        for i, g in enumerate(partidas):
            print(f'  No jogo {i} fez {g} gols.')
    print('-'*30)