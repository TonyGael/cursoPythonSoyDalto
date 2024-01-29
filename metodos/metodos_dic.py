'''
keys() -> devuelve las claves (permite iterar)
get() -> devuelve el valor de una clave
clear() _> elimina todos los elementos
pop() -> elimina un elemento
items() -> para iterar el diccionario
'''

diccionario = {
    "nombre" : "Tony",
    "apellido" : "Gael",
    "edad" : 39
}


claves = diccionario.keys()
print(claves)

clave = diccionario.get("apellido")
print("Seleccionada clave: " + clave)
 
#eliminando elementos con clear()
diccionario.clear()
print(diccionario)

diccionario1 = {
    "nombre" : "Tony",
    "apellido" : "Gael",
    "edad" : 39,
    "ciudad" : "Posadas"
}

print(diccionario1)
print("Eliminando con pop():")
diccionario1.pop("nombre")
print(diccionario1)
diccionario1.pop("apellido", "edad")
print(diccionario1)

#obtenemos un elemento dict_items
dicc_iterable = diccionario1.items()
print(dicc_iterable)
