from time import sleep

'''
Exercício Python 030: 
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
print('=' * 20)
print('O NUMERO É IMPAR OU É PAR? ')
print('=' * 20)
n = int(input('ENTRE COM UM NÚMERO: '))
if n % 2 == 0:
    print('O NUMERO É PAR')
else:
    print('O NUMERO É IMPAR')
