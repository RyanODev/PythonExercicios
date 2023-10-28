from random import randint

print('\033[34m-=-' * 20)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual foi?''')
print('-=-' * 20, '\033[m')

num = int(input('Qual o seu palpite? '))
computador = randint(0, 10)
tentativas = 0
while num != computador:
    if num > computador:
        num = int(input('Menos... Tente outro número: '))
    elif num < computador:
        num = int(input('Mais... Tente outro número: '))
    tentativas += 1
print('Parabéns!')
print('Você precisou de {} tentativas para acertar!'.format(tentativas + 1))
