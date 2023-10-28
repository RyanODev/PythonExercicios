a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

# Verificando quem é menor
menor = a
if b<a and b<a:
    menor = b
if c<a and c<b:
    menor = c

# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor foi {}{}{}'.format('\033[31m', menor, '\033[m'))
print('O maior valor foi {}{}{}'.format('\033[34m', maior, '\033[m'))
