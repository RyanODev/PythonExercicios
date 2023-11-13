from datetime import date
cadastro = {}
# ----------------------------------------------
cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = date.today().year - nascimento
cadastro['CTPS'] = int(input('CTPS[0 não tem]: '))
#------------------------------------------------
if cadastro['CTPS'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Ano de Contratação'] + 35) - date.today().year)
#-------------------------------------------------
print('-='*30)
for k, v in cadastro.items():
    print(f'  - {k}: {v}')
