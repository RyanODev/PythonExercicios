pessoa = {}
galera = []
soma = media = 0
mulheres = []
#-------------------------------------------------
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    sexo = ' '
#-----------------------------------------------------------------
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]')).strip().upper()
        if sexo not in 'MF':
            print('ERRO! POR FAVOR, DIGITE APENAS M OU F.')
        else:
            pessoa['sexo'] = sexo
        if sexo == 'F':
            mulheres.append(pessoa['nome'][:])
#-----------------------------------------------------------------
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = ' '
#-------------------------------------------------------------------
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()
        if resp not in 'SN':
            print('ERRO! POR FAVOR, DIGITE APENAS S OU N.')
    if resp == 'N':
        break
media = soma / len(galera)
#---------------------------------------------------------------------
print('-='*30)
print(f'{galera}')
print('-='*30)
#----------------------------------------------------------------------
print(f'A)  Ao todo, temos {len(galera)} pessoas cadastradas')
print(f'B)  A média de idade é de: {media:.2f} anos')
print(f'C)  As mulheres cadastradas foram: ', end='')
#----------------------------------------------------------------------
for p in galera:
    if p['sexo'] in 'F':
        print(p['nome'], end='; ')
#-----------------------------------------------------------------------
print()
print('D)  Lista das pessoas que estão acima da média:')
for i in galera:
    if i['idade'] >= media:
        for k, v in i.items():
            print(f'  {k} = {v}', end='')
        print()
#------------------------------------------------------------------------
print('<<< ENCERRADO >>>')
