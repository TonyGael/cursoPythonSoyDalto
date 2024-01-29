comidas = ["papas fritas", "pizzas", "chinchulin", "frutas", "tartas"]

for comida in comidas:
    if comida == "chinchulin":
        continue
    print(f'Me voy a comer unas {comida}')

# evitar que el bucle siga ejecutandise
for comida in comidas:
    print(f'Me voy a comer unas {comida}')
    if comida == "chinchulin":
        break
print("blucle terminado")

# recorrer una cadena de texto
cadena = "smartphone motorola"
for letra in cadena:
    print(letra)


# for en una sola linea de codigo
numeros = [1, 3, 5, 7, 9]
# numeros_duplicados = list()
# for num in numeros:
#     numeros_duplicados.append(num+1)

numeros_duplicados = [num+1 for num in numeros]
print(numeros_duplicados)
