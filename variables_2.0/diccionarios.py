diccionario = {
    'name' : 'Tony',
    'last_name' : 'Gael'
}

print(diccionario)

# creando diccionarios con dict
diccionario1 = dict(name = "Tony", last_name = "Gael")
print(diccionario1)

# creando un diccionario con fromkeys:
diccionario2 = dict.fromkeys("name", "last_name") # en este caso el primer parametro es un iterable
print(diccionario2)

diccionario3 = dict.fromkeys(["name", "last_name"])
print(diccionario3)
