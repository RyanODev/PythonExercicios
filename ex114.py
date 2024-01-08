import urllib.request


try:
    urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mNão é possível acessar o site no momento :(\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')