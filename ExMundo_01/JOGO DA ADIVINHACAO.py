from random import randint
from time import sleep
print('--=--'*20)
print('Vou pensar em um número de 0 a 5. Tente advinhar!')
print('--=--'*20)
n = randint(1, 5)
resp = int(input('Que número eu pensei ? '))
print('PROCESSANDO....')
sleep(2)
if resp == n:
    print('--=--' * 20)
    print('Isso mesmo, eu pensei no {} você é o cara!'.format(n))
    print('--=--' * 20)
else:

    print('--=--' * 20)
    print('Que pensa tu errou. Eu pensei no número {}'.format(n))
    print('--=--' * 20)