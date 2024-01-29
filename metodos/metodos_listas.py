#lista = list("Tony", "Gael", 39) #list expected at most 1 argument, got 3
lista = list(["Tony", "Gael", 39])
print(lista)

resultado = len(lista)
print(resultado)

add_append = lista.append("Learning Python")
print(lista)
print(type(add_append))

lista.insert(3, "19/12/2023")
print(lista)

lista.extend([False, True, 10.5, 20, "Chichat"])
print(lista)

lista.pop(1)
print(lista)
lista.pop(-1)
print(lista)
lista.pop(-2)
print(lista)

lista.remove("Tony")
print(lista)
#lista.sort() ypeError: '<' not supported between instances of 'str' and 'int'

lista_a_ordenar = [12,754,1,565,5.2]
lista_a_ordenar.sort()
print(lista_a_ordenar)
lista_a_ordenar.sort(reverse=True)
print(lista_a_ordenar)

lista_a_ordenar2 = list(["u", "a", "i", "e", "o"])
lista_a_ordenar2.sort()
print(lista_a_ordenar2)

#metodos de lista
print("Metodos de listas:")
print(dir([1,2]))

#metodos de tuplas
print("Metodos de tuplas:")
print(dir((1,)))

#metodos de diccionarios
print("Metodos de diccionarios:")
print(dir({"clave" : "valor"}))

#metotos de cojuntos de datos
print("Metodos de conjuntos de datos:")
print(dir(set(["hola", 1, True])))
