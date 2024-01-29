'''
¿Qué es el desempaquetado de variables?
    En Python, "Desembalaje de variables" es una operación de asignación especial .
    Le permite asignar todos los miembros de un objeto iterable (como list, set)
    a múltiples variables a la vez.
'''
# creando datos:
names_en_tupla = ("Tony", "Gael", 39)
names_en_lista = ["Tony", "Gael", 39]

# dessempaquetado:
name, last_name, age = names_en_tupla
print(f'Datos desempaquetados desde una tupla: {name} {last_name}, edad: {age}')
print(f'Datos desempaquetados desde una lista: {name} {last_name}, edad: {age}')
