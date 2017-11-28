''''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
print('-=-' * 20)
print('Analisador completo')
print('-=-' * 20)

mediaIdade = 0
nomeMaisvelho = ''
menosdeVinte = 0
velho  =0
for i in range(1, 4):

    nome = input('DIGITE SEU NOME: ')
    idade = int(input('DIGITE SUA IDADE: '))
    sexo = input('DIGITE O SEXO M / F :')
    mediaIdade += idade
    print('-=-' * 20)
    if i == 1:
        velho = idade
        print(velho)
    else:
        if idade > velho:
            nomeMaisvelho = nome
            print(velho)
    if 'f' == sexo or sexo == 'F':
        if idade < 20:
            menosdeVinte +=1


'''print('O NOME DA PESSOA MAIS VELHA: {}'.format(nomeMaisvelho))
print('NO GRUPO TEM {} MULHERES COM MENOS DE 20 ANOS'.format(menosdeVinte))
print('A MEDIA DE IDADE DO GRUPO É {} '.format(mediaIdade/4))'''