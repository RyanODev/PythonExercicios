dicionario = {}
lista = []

dicionario['Nome'] = str(input('Nome do jogador: '))
quantidade = int(input(f'Quantas partidas {dicionario["Nome"]} jogou?: '))
for c in range(1, quantidade + 1):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
dicionario['Gols'] = lista[:]
dicionario['Total de Gols'] = sum(lista)
print('-='*30)
print(dicionario)
print('=-'*30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor: {v}')
print('-='*30)
print(f'O jogador {dicionario["Nome"]} jogou {quantidade} partidas')
for i, v in enumerate(lista):
    print(f'   => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {dicionario["Total de Gols"]} gols')
