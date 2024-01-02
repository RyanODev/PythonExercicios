def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade <= 18 or idade > 60:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print('='*30)
ano_nasc = int(input('Ano de Nascimento: '))
print(voto(ano_nasc))