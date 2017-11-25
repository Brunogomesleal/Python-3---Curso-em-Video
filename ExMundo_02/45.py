from datetime import date
from random import choice
from time import  sleep

print('-=-' * 20)
print('Pedra, papel e tesoura')
print('-=-' * 20)
# AQUI IREI COLETAR OS DADOS PARA TOMA DE DEC. USEI A FUNC CHOICE DA BIB RABDOM PARA ISSO
jogador = input('VAMOS LÁ! ESCOLHA:\nPEDRA \nPAPEL\nTESOURA\n:MAIUSCULA:\n')
computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
#AQUI IREI COMPRAR AS ESCOLHAS E APRENSETAR OS RESULTADOS
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

#AQUI IREI IMPRIMIR AS ESCOLHAS DO JOGADORES MAQUINA / USUARIO
print('-=-' * 20)
print('O COMPUTADOR ESCOLHEU {} '.format(computador))
print('VOCÊ ESCOLHEU {}'.format(jogador))
print('-=-' * 20)
#FIZ DOIS IF'S ANINHADOS AQUI PARA PREVER AS DUAS HIPOTESES.
if jogador == 'PEDRA' and computador == 'TESOURA':
    print('Pedra ganha da tesoura (amassando-a ou quebrando-a).')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('Pedra ganha da tesoura (amassando-a ou quebrando-a).')
#FIZ DOIS IF'S ANINHADOS AQUI PARA PREVER AS DUAS HIPOTESES.
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('Tesoura ganha do papel (cortando-o).')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('Tesoura ganha do papel (cortando-o).')
#FIZ DOIS IF'S ANINHADOS AQUI PARA PREVER AS DUAS HIPOTESES.
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('Papel ganha da pedra (embrulhando-a).')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('Papel ganha da pedra (embrulhando-a).')
if jogador == computador:
    print('EMPATE! VAMOS JOGAR DE NOVO!')