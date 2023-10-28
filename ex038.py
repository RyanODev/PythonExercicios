a = float(input('Digite um valor: '))
b = float(input('Digite outro valo: '))

if a > b:
    print('O \033[34mPRIMEIRO\033[m valor é maior')
elif b > a:
    print('O \033[34mSEGUNDO\033[m valor é maior')
elif b == a:
    print('Não existe valor maior, os dois são \033[34mIGUAIS\033[m!')