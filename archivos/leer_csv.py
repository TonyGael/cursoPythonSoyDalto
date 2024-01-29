import csv # es el modulo csv de Python

with open('./archivos/texto.csv') as archivo:
    
    print('Datos leídos correctamente')
    # print(archivo.read())
    # print(csv.reader(archivo))
    readed = csv.reader(archivo)
    print(readed)
    
    for row in readed:
        print(row)
