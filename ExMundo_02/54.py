from time import sleep
from datetime import date

print('-=-' * 20)
print('Grupo da Maioridade')
print('-=-' * 20)

listaDePessoas = []
maiorIdade = 0
menorIdade = 0
for i in range(1, 8):
    listaDePessoas.append(int(input('ENTRE COM O ANO DE NASCIMENTO DA {}º PESSOA: '.format(i))))

for i in range(len(listaDePessoas)):
    idadeAtul = date.today().year - listaDePessoas[i]
    if idadeAtul >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1

print(' AO TODO  {} É MAIOR DE IDADE '.format(maiorIdade))
print('E,  {} PESSOA(S) SÃO MENOR(ES) DE IDADE'.format(menorIdade))
