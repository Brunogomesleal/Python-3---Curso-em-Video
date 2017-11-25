import  sys
print('=' * 20)
try:
    n1= float(input('N 1: '))
    n2 =  float(input('N 2: '))
except ValueError:
    print('Operação invalida! Favor verifique: ! {} / {}'.format(n1, n2))
except ValueError:
    print('Operação invalida! Favor verifique: ! {} / {}'.format(n1, n2))


try:
    div  =  n1/n2
    print(div)
except :
    error = sys.exc_info()[0]
    print(error)
    #print('Operação invalida! Favor verifique: ! {} / {}'.format(n1, n2))
