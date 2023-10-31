'''contF = 0
contA = 0
funcao = str(input('Digite uma função: '))
pilha = [funcao.split(funcao)]
for simb in funcao:
    if simb == '(':
        contA += 1
for simb in funcao:
    if simb == ')':
        contF += 1
if contA > contF or contF > contA:
    print('Sua função é inválida!')
elif contF == contA:
    print('Sua função funciona!')
print(f'Foram {contA} parênteses abrindo')
print(f'E {contF} parênteses fechando')''' # minha forma diferente de fazer o exercício!

# Forma do professor Guanabara:

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
