from datetime import date

print('-=-' * 20)
print('SISTEMA DE PAGAMENTO')
print('-=-' * 20)
produto = input('NOME DO PRODUTO: ')
valorProd = float(input('VALOR DO PRODUTO: '))
cond = int(input('FORMA DE PAGAMENTO:\n(1) - A VISTA  \n(2) A PRAZO)\n: '))
if cond == 1:
    condAvista = int(input('1 - DINHEIRO / CHEQUE \n2 - CARTÃO DE CRÉDITO '))
    if condAvista ==1:
        valorFinal = valorProd - (valorProd*0.10)
        print('PRODUTO: {}'.format(produto))
        print('TOTAL: R$ {}'.format(valorFinal))
    elif condAvista ==2:
        valorFinal = valorProd - (valorProd*0.05)
        print('PRODUTO: {}'.format(produto))
        print('TOTAL: R$ {:.2f}'.format(valorFinal))
elif cond == 2:
    qtdParcelas = int(input('QUANTAS PARCELAS: '))
    if qtdParcelas == 2:
        valorFinalParcelado = valorProd / qtdParcelas
        print('TOTAL: R$ {}'.format(valorProd))
        print('TOTAL DE PARCELAS {} X {}'.format(qtdParcelas, valorFinalParcelado))
    elif qtdParcelas >= 3:
        valorFinalComJuros = valorProd + (valorProd*0.20)
        valorFinalParcelado = valorFinalComJuros / qtdParcelas
        print('TOTAL: R$ {}'.format(valorFinalComJuros))
        print('TOTAL DE PARCELAS {} X {}'.format(qtdParcelas, valorFinalParcelado))
else:
    print('VALOR ERRADO!')
