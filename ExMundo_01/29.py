from time import sleep
'''
Exercício Python 029: 
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
'''
print('='*20)
print('RADAR ELETRONICO -  BRASIL UM PAÍS CORRUPTO')
print('='*20)
vel = int(input('VELOCIDADE EM KM/H ATINGIDA: '))
multa = (vel-80)*7
print('PROCESSANDO.....')
sleep(2)
if vel>80:
    print('=' * 20)
    print('VELOCIDADE ACIMA DO PERMITIDO, 80Km/h ')
    print('MULTA GERADA VALOR: R$ {}'.format(multa))
    print('=' * 20)
else:
    print('=' * 20)
    print('MOTORISTA DENTRO DA VELOCIDADE PERMITIDA!')
    print('DIRIGA COM SEGURANÇA')
    print('=' * 20)
