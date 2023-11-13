alunos_notas = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 01: '))
    n2 = float(input('Nota 02: '))
    media = (n1 + n2) / 2
    alunos_notas.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar?[S/N]')).upper().strip()
    if 'N' in resp:
        break
print('-=-'*10)
print(f'{"Nª.":4} {"NOME":15} {"MÉDIA"}')
print('-'*30)
for index, nome in enumerate(alunos_notas):
    print(f'{index:<5}', end=''), print(f'{nome[0]:17}', end=''), print(alunos_notas[index][2])
while True:
    resp2 = int(input('Quer ver as notas de qual aluno?(999 interrompe): '))
    if resp2 == 999:
        print('Finalizando...')
        break
    if resp2 < len(alunos_notas) - 1:
        print('-'*30)
        print(f'Notas de {alunos_notas[resp2][0]} são {alunos_notas[resp2][1][:2]}')
        print('-'*30)
print('<<<< VOLTE SEMPRE! >>>>')