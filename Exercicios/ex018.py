import math
angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor {} tem o SENO de {:.2f} graus'.format(angulo, seno))
print('O valor {} tem o COSENO de {:.2f} graus'.format(angulo, coseno))
print('O valor {} tem a TANGENTE de {:.2f} graus'.format(angulo, tangente))
