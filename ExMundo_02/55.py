print('-=-' * 20)
print('Maior e menor da sequência')
print('-=-' * 20)

listaDePeso = []
maiorPeso = 0
menorPeso = 0
for i in range(1, 6):
    listaDePeso.append(float(input('ENTRE COM O PESO KG DA {}º PESSOA: '.format(i))))

for i in range(len(listaDePeso)):
    #NO PRIMEIRO LAÇO PEGAR O VALOR E COLOCAR TANTO NO MENOR QUANTO NO MAIOR PESO
    if i == 0:
        maiorPeso = listaDePeso[i]
        menorPeso = listaDePeso[i]
    #DEPOIS SÓ COMPRAR COM OS VALORES DO PRIMEIRO LAÇO ATÉ O ULTIMO.
    else:
        #DUAS CONDIÇÕES SIMPLES PARA VERIFICAR O MAIOR E MENOR PESO
        if listaDePeso[i] > maiorPeso:
            maiorPeso = listaDePeso[i]
        if listaDePeso[i] < menorPeso:
            menorPeso = listaDePeso[i]


print('O MAIOR PESO LIDO FOI: {} '.format(maiorPeso))
print('O MENOR PESO LIDO FOI: {} '.format(menorPeso))

