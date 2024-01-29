numeros = (4, 7, 1, 42, 15, 5)

numero_mas_alto = max(numeros)
print(numero_mas_alto)

numero_mas_bajo = min(numeros)
print(numero_mas_bajo)


numero = round(12.321456, 2)
print(numero)


# funcion bool -> 0, vacio, False, None \\ True -> =! 0, TRue, cadena
res_bool = bool(0)
print(res_bool)

res_bool = bool()
print(res_bool)

res_bool = bool([])
print(res_bool)

res_bool = bool(None)
print(res_bool)

res_bool = bool(1)
print(res_bool)

res_bool = bool(True)
print(res_bool)

res_bool = bool('cadena')
print(res_bool)

# all -> retorna TRue si todos los elementos son verdaderos
res_all = all([234, "True", [344, 23]])
print(res_all)

sum_total = sum(numeros)
print(sum_total)
