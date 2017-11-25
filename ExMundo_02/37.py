from time import sleep

print('-=-'*20)
print('SISTEMA DE CONVERSÃO')
print('-=-'*20)
valorQualquer = int(input('Digite um valor para CONVERSÃO: '))
escolha = int(input('ESCOLHA A BASE PARA CONVERSÃO \n(1) PARA BINÁRIO \n(2) PARA OCTAL \n(3) PARA HEXADECIMAL\n:'))
sleep(3)
if escolha == 1:
    print('O valor digitado em BINARIO:\n{}'.format(bin(valorQualquer)))
elif escolha == 2:
    print('O valor digitado em OCTAL:\n{}'.format(oct(valorQualquer)))
elif escolha == 3:
    print('O valor digitado em HEXADECIMAL:\n{}'.format(hex(valorQualquer)))
else:
    print('ESCOLHA INCORRETA: ')
