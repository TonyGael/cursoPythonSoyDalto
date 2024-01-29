# lista:

lista = ["Tony", "Student", True, 1.70]
print(lista)
print(lista[1])
lista[1] = "Kinga"
print(lista[1])

# tupla:
# la tupla a diferencia de la lista no se puede modificar

tupla = ("Tony", "Student", True, 1.70)
print(tupla[0])
#tupla[1] = "Kinga"

# set
# se puede redefinr pero no modificar su valor interno, si alterar su orden por ejemplo
setDatos = {"Tony", "Student", True, 1.70}
# no se accede por medio del indice
#print (setDatos[1])
setDatos = {"Tony", "Student", True, 1.70, "Tony"}

# diccionario:

diccionario = {
    'nombre' : "Anthony",
    'apellido' : "Mayol",
    'booleano' : True,
    'altura' : 1.70,
    'duplicado' : True
}

print(diccionario['booleano'])

