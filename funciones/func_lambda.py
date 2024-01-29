# cerabdo una funcion lambda que multiplica por 2
# retornan automaticamente el valor
funcion_lambda = lambda x: x*2 # lambda es una manera de crear una funcion anonima

lambdita = funcion_lambda(3)
print(lambdita)
print(funcion_lambda(4))

# usando filter con funcion lambda:
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# funcion calcula par
def es_par(num):
    if(num % 2 == 0):
        return True

# ussando filter con una función común
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

# cramos para impar con lamda
numeros_impares = filter(lambda numero_impar: numero_impar % 2 == 1, numeros)
print(list(numeros_impares))
