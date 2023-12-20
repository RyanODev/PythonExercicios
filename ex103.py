def ficha(jogador='', gols=0):
    jogador = jogador
    gols = gols
    print('='*60)
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


print('-'*30)
j = str(input('Nome do jogador: '))
g = input('Quantidade de gols: ')
ficha(j, g)