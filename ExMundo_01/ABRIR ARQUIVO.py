import csv
#

file = 'bryophytesdatabase.csv'
tipo = 'r'
with open(file, tipo) as arquivCSV :
    dadosArquivo = csv.reader(arquivCSV)

    for i in dadosArquivo :
        print(i)



