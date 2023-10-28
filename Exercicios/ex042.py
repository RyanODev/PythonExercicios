print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

s1 = float(input('|Seguimento 1: '))
s2 = float(input('|Seguimento 2: '))
s3 = float(input('|Seguimento 3: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('Os seguimentos acima PODEM formar um triângulo EQUILÁTERO!')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('Os seguimentos acima PODEM formar um triângulo ISÓCELES')
    elif s1 != s2 != s3 != s1:
        print('Os seguimentos acima PODEM formar um triângulo ESCALENO!')
else:
    print('Os seguimentos NÃO podem formar um triângulo!')