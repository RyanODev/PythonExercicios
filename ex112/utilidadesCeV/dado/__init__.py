def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'\033[31mERRO! "{entrada}" É UM PREÇO INVÁLIDO!\033[m')
        else:
            valido = True
            entrada = float(entrada)
            return entrada

