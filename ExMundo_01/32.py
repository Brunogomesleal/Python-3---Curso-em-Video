from datetime import date
'''''
Exercício Python 032:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

print('=' * 20)
print('ANO BISEXTO ')
print('=' * 20)
n = int(input('DIGITE UM ANO: '))
if n==0:
    n = date.day
if n % 4 == 0 and n %100 != 0 or n % 400 == 0:
    print('O ANO É BISEXTO')
else:
    print('O ANO NÃO É BISEXTO')