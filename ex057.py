sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados icorretos. Digite novamente! ')).upper()
print('Sexo {} registrado com sucesso!'.format(sexo))