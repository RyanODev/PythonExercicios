colocacao = ('Botafogo', 'Bragantino', 'Flamengo', 'Atlético-PR', 'Grêmio',
             'Palmeiras', 'Atlético-MG', 'Fortaleza', 'Fluminense', 'São Paulo', 'Cuiabá', 'Bahia', 'Internacional',
             'Corinthians', 'Cruzeiro', 'Chapecoense', 'Goiás', 'Vasco da Gama', 'Santos', 'Coritiba', 'América-MG')
print('Os primeiros 5 colocados são:')
for a in colocacao[0:5]:
    print(a)
print('='*50)
print('Os últimos 4 colocados são:')
for b in colocacao[-4:]:
    print(b)
print('='*50)
print('Segue os times em ordem alfabética:\n', sorted(colocacao))
print('='*50)
print(f'O time Chapecoense está na posição: {colocacao.index("Chapecoense")+1}')