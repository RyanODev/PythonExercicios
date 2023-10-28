# importar a biblioteca pygame
import pygame
# inicializar o pygame
pygame.init()
# carregar o audio/musica
pygame.mixer.music.load('waves.mp3')
# dar play na música
pygame.mixer.music.play()
# entrada da música
input()
# só finalizar o programa quando a música acabar
pygame.event.wait()


'''from playsound import playsound

playsound('waves.mp3')
print('rodando uma música usando  playsound')'''