# Creamos una sucesión de fobonacci entre 0 y el nñumero dado

def fibonacci(num):
    a,b = 0, 1
    lista_fibonacci = [0]
    for i in range(num):
        if b > num:
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a,b = b, a+b
    return lista_fibonacci

resultado = fibonacci(50)
print(resultado)
