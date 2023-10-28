print('-=-' * 20)
print('Analisador de IMC...')
peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua altura(m): '))
print('-=-' * 20)

imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbita!')