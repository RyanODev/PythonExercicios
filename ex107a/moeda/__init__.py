def metade(n):
    met = n / 2
    return met

def dobro(n):
    dob =  n * 2
    return dob

def aumentar(n1, n2):
    aumen = (n2 * n1) / 100
    return aumen + n1
    

def diminuir(n1, n2):
    dimin = n1 - ((n1 * n2) / 100)
    return dimin

def moeda(n):
    return f'R${n:.2f}'