def nota(*num, sit=False):
    '''
    nota(*num, sit=False)
        --> Função para analisar notas e situação das alunos
        param num: uma ou mais notas dos alunos(aceita várias notas).
        pram sit: parâmtro opcional para mostrar a situação dos alunos.
        return: dicionário de várias informações e situação da turma.
    '''
    d = dict()
    
    d['Quantidade'] = len(num)
    d['Menor'] = min(num)
    d['Maior'] = max(num)
    d['Média'] = sum(num) / len(num)
    
    if sit == True:
        if d['Média'] < 6:
            situacao = 'RUIM'
        if d['Média'] >= 6:
            situacao = 'RAZOAVEL'
        if d['Média'] >= 7.5:
            situacao = 'BOA'
        if d['Média'] >= 9:
            situacao = 'ÓTIMA'
        d['Situação'] = situacao
    
    return d
    


resp = nota(6, 6.5, 8, 9.5, sit=True)
print(resp)