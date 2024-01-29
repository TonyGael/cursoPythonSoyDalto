with open('./archivos/texto.txt', 'a', encoding='UTF-8') as archivo:
    # agregando al archivo
    archivo.write('\nLoL así no era wey!')
    for i in range(5):
        archivo.write(f'Linea {i+1} agregada\n')
