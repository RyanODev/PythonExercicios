from random import randint
c = ['\033[0;30;41m',
         '\033[0;30;42m', # VERDE
         '\033[0;30;43m',
         '\033[0;30;44m',
         '\033[0;30;45m',
         '\033[0;30;46m', #CIANO
         '\033[0;30;47m',
         '\033[7;40m'
        ]


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{comando}\'')
    print(c[7])
    help(com)
    print(c[7])

def titulo(msg, cor=1):
    tam = len(msg) + 4
    print(c[cor])
    print('=' * tam)
    print(f'  {msg}  ')
    print('=' * tam)
    print(c[cor])



while True:
    titulo('Sistema de Ajuda Pyhelp')
    comando = str(input('\033[mFunção ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')