frase = input("Dime na frase y te digo cuanto tardarías en decirla: ")
palabras_separadas = frase.split(" ")
print(palabras_separadas)
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, tardarías {cantidad_de_palabras/2} segundos en decirlas.')
print(f'Dalto tardaría {cantidad_de_palabras / 2 / 1.3} segundos en decirlas.')

if cantidad_de_palabras > 120:
    print("Menos palabras por favor!")
