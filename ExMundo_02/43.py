from datetime import date

print('-=-' * 20)
print('IMC')
print('-=-' * 20)
peso = float(input('PESO: '))
altura = float(input('ALTURA: '))
imc = peso/(altura*altura)
if imc <18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >=25 and imc <30:
    print('SOBREPESO')
elif imc >=30 and imc <40:
    print('OBESIDADE')
elif imc >40:
    print('OBESIDADE MORBIDA')