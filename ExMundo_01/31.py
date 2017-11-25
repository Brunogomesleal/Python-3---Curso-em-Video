from time import sleep

''''
Exercício Python 031: 
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
print('=' * 20)
print('SISTEMA DE PASSAGENS - BRASIL UM PAÍS CORRUPTO')
print('=' * 20)
dist = float(input('DISTANCIA DA VIAGEM:'))
passagem = dist
if dist<=200:
    passagem = dist*0.5
    print('VALOR/PASSAGEM: R$ {}'.format(passagem))
elif dist>200:
    passagem = dist*0.45
    print('VALOR/PASSAGEM: R$ {}'.format(passagem))


