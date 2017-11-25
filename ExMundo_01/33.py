from datetime import date

'''''
Exercício Python 033: 
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

print('=' * 20)
print('QUAL MENOR NUMERO ')
print('=' * 20)
lista = []

for i in range(1, 4):
    lista.append(int(input('Digite {}º NUMERO: '.format(i))))

print ("\nMenor valor:", min(lista), "\nMaior valor:", max(lista))
