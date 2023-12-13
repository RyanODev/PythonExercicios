def escreva(msg):
    tam = len(msg) + 4
    print(f"{'~'}" * tam)
    print(f'  {msg}')
    print(f"{'~'}" * tam)


escreva('Curso em Vídeo')
escreva('My name')