salario = float(input('Quanto o funcionário recebe? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem recebe \033[1;31mR${:.2f}\033[m passa a ganhar \033[1;32mR${:.2f}\033[m'.format(salario, novo))
