"""
¿Qué es un métodos en Python?
    Un método es una función que «pertenece a» un objeto. En Python,
    el término método no está limitado a instancias de clase:
    otros tipos de objetos pueden tener métodos también.
    Por ejemplo, los objetos lista tienen métodos llamados
    append, insert, remove, sort, y así sucesivamente.
"""

cadena1 = "abc, 123, 45, 67,89, 0, abc"
cadena2 = "Welcome to my path learning :-)"

#resultado = dir(cadena1)
#resultado = cadena1.upper()
#resultado = cadena1.lower()
#resultado = cadena1.capitalize()

# a continuación estaríamos retornando valores

# busqueda_find = cadena1.find("Gael")
# print(busqueda_find)

#busqueda_index = cadena1.index("t") # lanza excepción sinó halla el valor
#print(busqueda_index)

# es_numerico = cadena1.isnumeric()
# print(es_numerico)
# es_alfabetico = cadena1.isalpha()
# print(es_alfabetico)
# es_alfanumerico = cadena1.isalnum()
# print(es_alfanumerico)

contar_coincidencia = cadena1.count("0 a")
print(contar_coincidencia)

contar_caracteres = len(cadena1)
print(contar_caracteres)

empieza_con = cadena1.startswith("a")
print(empieza_con)

termina_con = cadena1.endswith("abc")
print(termina_con)

cadena_nueva = cadena1.replace("abc", "numbers")
print(cadena1)
print(cadena_nueva)

cadena_separada = cadena1.split(",")
print(cadena_separada)
print(type(cadena_separada))

