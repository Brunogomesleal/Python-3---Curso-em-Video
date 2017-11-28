print('-=-' * 20)
print('CONTAGEM DOS PARES')
print('-=-' * 20)

for i in range(1, 51):
    cont = 0
    if i % 2 == 0:
        cont += i
        print(cont)
