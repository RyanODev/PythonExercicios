def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano

    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA!')
    elif idade >= 60:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')


print('='*30)
ano_nasc = int(input('Ano de Nascimento: '))
voto(ano_nasc)