from random import randint
from time import sleep

print('-=-' * 30) # imprime 30x esses simbolos
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 30)

n = int(input('Em que número pensei? '))
print('Processando...')
sleep(1)

a = randint(0, 5)    # randomiza um número aleatório entre 0 e 5

if n == a:     # se n for igual a 'a', imprimir a primeira opção
    print('Você acertou! Como sabia que eu tinha pensado nesse número?... poxa!')
else: # se não, imprimir a segunda opção
    print('Você errou! EU GANHEI DE VOCÊ!')

