from time import sleep
distancia = float(input('Qual a distância da sua viagem? '))

print('-=-' * 30)
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
print('Calculando o valor da passagem...')
print('-=-' * 30)
sleep(1)

if distancia <= 200:
    calculo = distancia * 0.50
    print('O preço de sua passagem será de R${:.2f} REAIS'.format(calculo))
else:
    calculo = distancia * 0.45
    print('O preço da sua passagem será de R${:.2f}'.format(calculo))