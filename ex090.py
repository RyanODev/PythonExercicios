situacao = ' '
dicionario = {}
for c in range(0,1):
    dicionario['Nome'] = str(input('Nome do Aluno: '))
    dicionario['Média'] = float(input(f'Média de {dicionario["Nome"]}: '))
if dicionario['Média'] >= 7:
    dicionario['Situação'] = 'Aprovado'
elif dicionario['Média'] >= 5:
    dicionario['Situação'] = 'Recuperação'
else:
    dicionario['Situação'] = 'Reprovado'
print('='*30)
for k, v in dicionario.items():
    print(f'- {k} = {v}')