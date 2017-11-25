from time import sleep

print('-=-'*20)
print(': SISTEMA DE FINANCIAMENTO :')
print('-=-'*20)
# AQUI IREI COLETAR OS DADOS PARA TOMA DE DEC.
vCasa = float(input('VALOR CASA: R$ '))
vSalario = float(input('RENDIMENTO MENSAL: '))
qtdAnos = int(input('QUANTIDADE DE ANOS P/ PAGAMENTO: '))*12
#AQUI IREI CALCULAR TUDO. SER REALISTA
prestMensal = vCasa/qtdAnos
excSalario = (vSalario*0.30)-prestMensal
sleep(3)
#AQUI IREI TOMAR A DEC DE ACORDO COM OS CALCULOS E IMPRIMIR O RESULTADO
if excSalario >=0:
    print('TERMOS: \n')
    print('VALOR DA CASA: R$ {}'.format(vCasa))
    print('MENSALIDADE: R$ {}'.format(prestMensal))
    cond = input('ACEITAR OS TERMO: S/N')
    if cond == 'S':
        print('PARABÉNS PELA COMPRA! ')
    else:
        print('OBRIGADO PELA PREFERENCIA!')
else:
    print('PROPOSTA NEGADA. RENDIMENTO INSUFICIENTE!  ')