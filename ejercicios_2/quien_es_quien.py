'''
Enunciado:
    1 Alumno es profesor
    1 alumno es asistente
    A) Pedir la edad de los compañeros que vinieron hoy a clases y ordenar los datos de menor a mayor
    b) El mayor es el profesor y el menor es el asistente
    ¿Quién es quién?
'''

# Ingresamos nombre y edad de los compañeros de clases 
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input(f'Ingrese nombre del compañero: ')
        edad = input(f'Ingrese la edad del compañero: ')
        compañero = (nombre, edad)
        compañeros.append(compañero)
    
    compañeros.sort(key = lambda compa: compa[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor
    

#compañeros = obtener_compañeros(3)
#print(list(compañeros))

#desempaquetando
asistente, profesor = obtener_compañeros(5)
print(f'El profesor temporal es {profesor} y su asistente es {asistente}.')

