from time import sleep
print('-=-' * 20)
print('Soma dos pares')
print('-=-' * 20)
# Aqui eu criei duas listas porque vou fazer uma lista só com os pares.
#Usei uma variavel SOMAPAR apenas para pegar a soma fora do for. porque irei usa-la mais tarde.
#Se ela ficar dentro do for eu não poderei usa-la depois
numbList = []
numbPar = []
somaPar = 0
#aqui carrego minha lista de numeros INTEIROS
for i in range(1, 7):
    numbList.append(int(input('DIGITE O {}º NUMERO INTEIRO: '.format(i))))
# aqui eu carrego minha lista com numeros PARES APENAS
for i in numbList:
    if i % 2 == 0:
        somaPar +=i
        numbPar.append(i)
#AQUI EU IMPRIMO MINHA LISTA COM OS NUMERO PARES QUE FOI USADO NA SOMA
print('NUMEROS SOMADOS SÃO:')
for i in numbPar:
    print(i, end="-")
#AQUI EU IMPRIMO A SOMA DOS PARES.
sleep(2)
print('')
print('-=-' * 15)
print('\nA SOMA  DE TODOS OS PARES É: {}'.format(somaPar))