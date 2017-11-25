print('-=-' * 20)
print('SISTEMA DE NOTAS')
print('-=-' * 20)
nota1 = float(input('PRIMEIRA NOTA: '))
nota2 = float(input('SEGUNDA NOTA: '))
mediaAluno = (nota1+nota2)/2

if mediaAluno < 5:
    print('REPROVADO!')
elif mediaAluno >= 5 and mediaAluno <= 6.9:
    print('RECUPERAÇÃO')
elif mediaAluno >= 7:
    print('APROVADO')