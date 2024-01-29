with open('./archivos/texto.txt', 'w', encoding='UTF-8') as archivo:
    # a continuación lo que sucederá es que se reescribirá el archivo
    #archivo.write('Hola ke hace?')
    
    archivo.writelines(['La llama que llama\n', 'Esta de regreso\n'])
    archivo.writelines(['La llama que llama\n', 'Esta de regreso\n'])
    archivo.writelines(['La llama que llama\n', 'Esta de regreso\n', 'La llama que llama\n', 'Esta de regreso\n'])
