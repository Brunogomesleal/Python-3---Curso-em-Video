from time import sleep
print('-=-' * 20)
print('Números primos')
print('-=-' * 20)

num = int (input('Digite um numero INTEIRO: '))
contPrimo = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', i, end='')
        contPrimo += 1
    else:
        print('\033[31m',i,  end='')
print('\n\033[30mO NUMERO {} FOI DIVISIVEL {} vezes '.format(num, contPrimo))

if contPrimo == 2:
    print('PORTANTO ELE É PRIMO!')
else:
    print('POR ISSO NÃO É PRIMO!')