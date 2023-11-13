from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(0, 6),
        'Jogador2': randint(0, 6),
        'Jogador3': randint(0, 6),
        'Jogador4': randint(0, 6)
        }
for k, v in jogo.items():
    print(f'{k} jogou o número {v} no dado')
    sleep(0.5)
lista = jogo
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
