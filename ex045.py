from time import sleep
import random
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada?: '))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.choice(lista)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=' * 10)
print('Jogador jogou: {}'.format(lista[jogador]))
print('Computador jogou: {}'.format(computador))
print('-=' * 10)

if jogador == 0: # Computador jogou PEDRA
    if computador == 'PAPEL':
        print('COMPUTADOR VENCE!')
    elif computador == 'PEDRA':
        print('EMPATE!')
    elif computador == 'TESOURA':
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')
elif jogador == 1: # Computador jogou PAPEL
    if computador == 'PAPEL':
        print('EMPATE!')
    elif computador == 'PEDRA':
        print('JOGADOR VENCE!')
    elif computador == 'TESOURA':
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')
elif jogador == 2: # Computador jougou TESOURA
    if computador == 'PAPEL':
        print('JOGADOR VENCE!')
    elif computador == 'PEDRA':
        print('COMPUTADOR VENCE!')
    elif computador == 'TESOURA':
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')
