'''
Exercício Python 014:
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
print('='*20)
celsius = float(input('TEMPERATURA EM Celsius: '))
convf = (celsius*1.8)+32
print('TEMPERATURA EM F {}'.format(convf))