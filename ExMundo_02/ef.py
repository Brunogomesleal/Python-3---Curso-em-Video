#coding: UTF-8
print('-=' * 10 + '=-' * 10 + '\n|\t\t\t   Desafio 45   \t\t\t|')
print('-=' * 10 + '=-' * 10)
from random import randrange
from os import system
system('title JanKenPon')
JanKenPon = {1:'Pedra', 2:'Papel', 3:'Tesoura', 4: 'Lagarto', 5: 'Spock'}
máquina = randrange(1,6)
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('4 - Lagarto')
print('5 - Spock')
usuário = int(input('Qual você escolhe?'))
print('Máquina: ' + JanKenPon[máquina])
print('Usuário: ' + JanKenPon[usuário])
if máquina == usuário:
    print('Empate!')
elif máquina == 1 and usuário == 2:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#1x2v
elif máquina == 1 and usuário == 3:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#1x3p
elif máquina == 1 and usuário == 4:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#1x4p
elif máquina == 1 and usuário == 5:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#1x5v
elif máquina == 2 and usuário == 1:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#2x1p
elif máquina == 2 and usuário == 3:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#2x3v
elif máquina == 2 and usuário == 4:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#2x4v
elif máquina == 2 and usuário == 5:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#2x5p
elif máquina == 3 and usuário == 1:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#3x1v
elif máquina == 3 and usuário == 2:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#3x2p
elif máquina == 3 and usuário == 4:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#3x4p
elif máquina == 3 and usuário == 5:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#3x5v
elif máquina == 4 and usuário == 1:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#4x1v
elif máquina == 4 and usuário == 2:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#4x2p
elif máquina == 4 and usuário == 3:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#4x3v
elif máquina == 4 and usuário == 5:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#4x5p
elif máquina == 5 and usuário == 1:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#5x1p
elif máquina == 5 and usuário == 2:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#5x2v
elif máquina == 5 and usuário == 3:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você perdeu!')#5x3p
elif máquina == 5 and usuário == 4:
    print(JanKenPon[máquina] + ' x ' + JanKenPon[usuário] + ': Você venceu!')#5x4v
