def ficha(jogador='', gols=0):
    jogador = jogador
    gols = gols
    print('=' * 60)
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


print('-' * 30)
j = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(j, g)
