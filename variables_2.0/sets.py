conjunto1 = set(["Data 1", "Data 2"])
print(f'conjunto1: {conjunto1}')

conjunto2 = set(["Dato1", ("Dato2", "Dato3")]) # tupla // solo pueden ir datos que no se muten
print(conjunto2)

#conjunto = set(["Dato1", {"dato2" : "D2", "dato3" : "D·"}]) # diccionario
print(conjunto2)

# tengamos en cuenta que lso datos de un set no so modificlabes

#metiendo n conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato1", "Dato2"])
conjunto2 = {conjunto1, "Dato3"}
print(conjunto2)

# conjuntos

conjunto_1 = {1, 5, 78, 100}
conjunto_2 = {5, 78}
resultado = conjunto_2.issubset(conjunto_1) # conjunto_2 <= conjunto_1
print(resultado)
resultado = conjunto_1.issuperset(conjunto_2) #conjunto_2 > conjunto_1
print(resultado)

# verificando si hay un numero e comun:
resultado = conjunto_2.isdisjoint(conjunto_1)
print(resultado)
