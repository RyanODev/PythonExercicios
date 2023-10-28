palavras = ('Python', 'Aprender', 'Futuro', 'Curso', 'Programacao')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end='')