'''
Exercício Python 034:
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

print('\33[0;34;0m=' * 20)
print('REAJUSTE SALARIO')
print('\33[0;34;0m=' * 20)
sal = float(input('Digite o valor do Salário: '))
reajuste = 0
if sal >= 1250:
    reajuste = (sal*0.10)+sal
    print('NOVO SALARIO: R$ {}'.format(reajuste))
else:
    reajuste = (sal*0.15)+sal
    print('NOVO SALARIO: R$ {}'.format(reajuste))
