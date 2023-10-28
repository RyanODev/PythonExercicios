a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura? '))
r = (a * l)
t = r / 2
print('Sua parede tem a dimensão de {:.2f} por {:.2f}, e sua área é de {:.2f}m².'.format(a, l, r))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta'.format(t))
