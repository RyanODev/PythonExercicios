def metade(n, formato=False):
    met = n / 2
    if formato == True:
        return f'R${met:.2f}'
    else:
        return met

def dobro(n, formato=False):
    dob =  n * 2
    if formato == True:
        return f'R${dob:.2f}'
    else:
        return dob

def aumentar(n1, n2, formato=False):
    aumen = (n2 * n1) / 100
    aumen += n1
    if formato == True:
        return f'R${aumen:.2f}'
    else:
        return aumen 
    

def diminuir(n1, n2, formato=False):
    dimin = n1 - ((n1 * n2) / 100)
    if formato == True:
        return f'R${dimin:.2f}'
    else:
        return dimin
    
def moeda(n):
    return f'R${n:.2f}'

def resumo(p=0, a=10, b=5):
    print('='*30)
    print(f'{'RESUMO DE VALOR':^30}')
    print('='*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Metade do preço: \t{moeda(metade(p))}')
    print(f'{a}% de aumento: \t{moeda(aumentar(p, a))}')
    print(f'{b}% de redução: \t{moeda(diminuir(p, b))}')
    print('='*30)
