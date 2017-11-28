print('-=-' * 20)
print('Soma ímpares múltiplos de três')
print('-=-' * 20)
contSoma = 0
contQtd = 0
for i in range(1, 501):
    if i % 2 !=0:
        if i % 3 == 0:
            contQtd += 1
            contSoma += i

print('A SOMA DE {} VALORE(S) MULTIPLOS DE 3 SÃO {}'.format(contQtd, contSoma))
