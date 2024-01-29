diccionario = {
    "name" : "Tony",
    "last_name" : "Gael",
    "age" : 39
}

for key in diccionario.items():
    print(key)


for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y el valor es: {value}')

