def metade(n, format=False):
    met = n / 2
    if format == True:
        return f'R${met:.2f}'
    else:
        return met

def dobro(n, format=False):
    dob =  n * 2
    if format == True:
        return f'R${dob:.2f}'
    else:
        return dob

def aumentar(n1, n2, format=False):
    aumen = (n2 * n1) / 100
    aumen += n1
    if format == True:
        return f'R${aumen:.2f}'
    else:
        return aumen 
    

def diminuir(n1, n2, format=False):
    dimin = n1 - ((n1 * n2) / 100)
    if format == True:
        return f'R${dimin:.2f}'
    else:
        return dimin
    
def moeda(n):
    return f'R${n:.2f}'

def resumo(p, a, b):
    print('='*30)
    print(f'{'RESUMO DE VALOR':^30}')
    print('='*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Metade do preço: \t{moeda(metade(p))}')
    print(f'80% de aumento: \t{moeda(aumentar(p, a))}')
    print(f'35% de redução: \t{moeda(diminuir(p, b))}')
    print('='*30)
