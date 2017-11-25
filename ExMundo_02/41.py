from datetime import date

print('-=-' * 20)
print('CONFEDERAÇÃO NACIONAL DE NATACAO')
print('-=-' * 20)

anoNascimento = int(input('ANO DE NASCIMENTO: '))
catAtleta = date.today().year - anoNascimento
if catAtleta <= 9:
    print('MIRIM')
elif catAtleta <= 14:
    print('INFANTIL')
elif catAtleta <= 19:
    print('JUNIOR')
elif catAtleta <= 20:
    print('SENIOR')
elif catAtleta > 20:
    print('MASTER')
