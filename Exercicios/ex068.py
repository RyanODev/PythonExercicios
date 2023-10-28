from random import randint
import pygame

pygame.mixer.init()
pygame.init()




cont = 0
resultado = resu = ''
while True:
    jogador = int(input('digite um número: '))
    escolha = str(input('Par ou Ímpar?[P/I]: ')).upper().strip()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    if escolha == 'P':
        if (jogador + computador) % 2 == 0:
            cont += 1
            resu = 'Ganhou'
        else:
            resu = 'Perdeu'
    elif escolha == 'I':
        if (jogador + computador) % 2 != 0:
            cont += 1
            resu = 'Ganhou'
        else:
            resu = 'Perdeu'
    print('=' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Deu ', end='')
    print('Par' if (jogador + computador) % 2 == 0 else 'Ímpar')
    print('=' * 30)
    if resu == 'Perdeu':
        pygame.mixer.music.load('loser.wav')
        pygame.mixer_music.play()
        pygame.event.wait(2)
        input()
        print('Você perdeu!')
        break
    if resu == 'Ganhou':
        print('Você ganhou!')
        pygame.mixer.music.load('goodresult.mp3')
        pygame.mixer_music.play()
        pygame.event.wait(2)
        print('Vamos continuar...')
        print('-'*30)
print(f'Game Over. Você venceu {cont} vezes.')