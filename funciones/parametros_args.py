# forma no optima de sumar valores
def suma(a, b):
    return a + b

resultado = suma(2,7)
print(resultado)

#otra forma no optima de sumar valores
def suma(lista):
    acum = 0
    for numero in lista:
        acum+=numero
    return acum

resultado = suma([2,3,5])
print(resultado)

# forma optima con parametro args
def suma(*numeros):
    return sum(numeros)

resultado = suma(4,5,6,7,8,9)
print(resultado)

def suma(nombre, *args):
    return f'{nombre}, la suma de tus números es: {sum(args)}'

resultado = suma('Tony', 1,2,3,4,5)
print(resultado)

def suma2(numeros):
    return sum([*numeros])# hay qe retornar como unalista

resultado = suma2([1,2,3,4,5])
print(resultado)
