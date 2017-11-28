from time import sleep
print('-=-' * 20)
print('Números primos')
print('-=-' * 20)

frase = str(input('DIGITE SUA FRASE: ')).strip().upper()
#explodo a frase em palavras em uma lista
palavras = frase.split()
#junto as palavras tirando o espaço
juntas = ''.join(palavras)
inverso =''

for i in range(len(juntas) - 1, -1, -1):
    inverso += juntas[i]
print('O INVERSO DA FRASE {} É {}'.format(juntas, inverso))
if inverso == juntas:
    print('TEMOS UM Palíndromo: '.format(juntas, inverso))