from time import sleep

print('-=-'*20)
print('COMPARANDO NUMEROS')
print('-=-'*20)
numero1 = int(input('VALOR 1: '))
numero2 = int(input('VALOR 2:'))

if numero1 == numero2:
    print('VALORES IGUAIS {} \ {}'.format(numero1, numero2))
elif numero1 >numero2:
    print('O NUMERO 1: {} É MAIOR QUE O  2: {}'.format(numero1, numero2))
else:
    print('O NUMERO 2: {} É MAIOR QUE O  1: {}'.format(numero2, numero1))