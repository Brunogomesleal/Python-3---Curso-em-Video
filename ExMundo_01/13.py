print('='*20)
func = input('FUNCIONARIO:')
sal = float(input('SALARIO:  '))
reajuste = sal+(sal*0.15)
print('NOVO SALARIO DO FUNCIONARIO: {} / R$ {:.2f} COM REAJUSTE '.format(func, reajuste))
print('='*20)