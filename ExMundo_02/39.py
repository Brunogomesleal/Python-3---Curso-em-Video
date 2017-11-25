from time import sleep
from datetime import date

print('-=-' * 20)
print('ALISTAMENTO/ GOVERNO FEDERAL')
print('-=-' * 20)
ano = int(input('ANO DE NASCIMENTO: '))
iddAtul = date.today().year - ano

if iddAtul < 18:
    cont = 18 - iddAtul
    print('AINDA TERÁ DE SE ALISTAR AO SERVIÇO MILITAR')
    print('AINDA FALTA {} ANO PARA VOCÊ SE ALISTAR'.format(cont))
elif iddAtul == 18:
    print('ESTÁ NA HORA DE SE ALISTAR')
    print('VOCÊ TEM QUE SE ALISTAR LOGO')
elif iddAtul >18:
    cont = iddAtul - 18

    print('VOCÊ DEVERIA TER SE ALISTADO HA {}'.format(cont))
    print('SEU ALISTAMENTO FOI EM {} '.format(date.today().year-cont))
