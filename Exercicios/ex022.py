nome = str(input('Qual é o seu nome? '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper())) # nome em maiúsculo
print('Seu nome em minúsculas é {}'.format(nome.lower())) # nome em minúsculo
print('Seu nome tem ao todo tem {} letras'.format(len(nome) - nome.count(' '))) # conta quantas letras tem sem considerar os espaços
dividido = nome.split() # divide a string em partes
print('Seu primeiro nome é {}, e tem {} letras'.format(dividido[0], len(dividido[0]))) # conta quantas letras tem da lista 0 = Ryan
# uma das formas de fazer a mesma coisa à cima
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
