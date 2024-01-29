# archivo = open('./archivos/texto.txt', encoding='UTF-8')
# print(archivo.read())

archivo_sin_leer = open('./archivos/texto.txt', encoding='UTF-8')
# archivo_leido = archivo_sin_leer.read()
# print(archivo_leido)

# lineas = archivo_sin_leer.readlines()
# print(lineas)

# leer una sola línea
linea_1 = archivo_sin_leer.readline()
print(linea_1)

# Si queremos cerrar el archivo
archivo_sin_leer.close()

print(linea_1)
