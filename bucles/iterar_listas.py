hardware = ["SSD", "HDD", "RAM", "Micro", "Mother"]

for hw in hardware:
    print(f'Hardware: {hw}')

numeros = [1, 2, 3, 4, 5]

for num in numeros:
    resultado = num * 10
    print(resultado)

for num, hw in zip(numeros, hardware):
    print(f'recorriendo lista 1: {num}')
    print(f'recorriendo lista 2: {hw}')

hardware_2 = ["SSD", "HDD", "RAM", "Micro", "Mother", "Video Card"]

for hw, num in zip(hardware_2, numeros):
    print(f'recorriendo lista hardware2: {hw}') # recorrera hasta el 5 item, deben teer el mismo tamaño
    print(f'recorriendo la lista numeros: {num}')

lista_numeros = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

for num in range(6,10):
    print(num)

for num in range(lista_numeros[2], lista_numeros[7]):
    print(num)

for numero in range(10):
    print(numero)

for numero in range(10,20):
    print(numero)

for num in range(len(lista_numeros)):
    print(f'Numero en la posicion {num}= {lista_numeros[num]}')

# la forma correcta es enumerate:
for num in enumerate(lista_numeros):
    print(num) # devuelve una tupla, primer parametro el indice, segundo parametro, el valor en ese indice 

for num in enumerate(lista_numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')


vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    print(f'ejecutando el ultimo bucle, valor actual: {vocal}')
else:
    print("el bucle termino")

# todo lo anterior funcina exactamente igual para las tuplas

