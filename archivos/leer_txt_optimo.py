with open('./archivos/texto.txt', encoding='UTF-8') as archivo:
    
    print('Esta sentencia se ejecuta si se abrió bien el archivo.')
    
    # leemos el archivo
    contenido = archivo.read()
    
    # mostramos el contenido
    print(contenido)

# print(archivo.read())
