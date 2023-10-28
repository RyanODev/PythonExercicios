from datetime import date
nascimento = int(input('Em que ano você nasceu? '))

print('''Qual o seu sexo?
Pressione [m] para Masculino
Pressione [f] para Feminino''')
sexo = str(input('Sua escolha: '))

atual = date.today().year
idade = atual - nascimento

if sexo == 'f':
    print('Pessoas do sexo FEMININO não precism prestar o Serviço Militar obrigatório!')
elif idade < 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
    tempo = 18 - idade
    ano = tempo + atual
    print('Faltam {} ano(s) para o alistamento!'.format(tempo))
    print('E será em {}'.format(ano))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
    print('Já tá na hora de se alistar!')
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
    tempo = idade - 18
    ano = atual - tempo
    print('Já passou da hora de se alistar!')
    print('Você deveria ter se alistado há {} anos.'.format(tempo))
    print('Seu alistamento foi em {}'.format(ano))
