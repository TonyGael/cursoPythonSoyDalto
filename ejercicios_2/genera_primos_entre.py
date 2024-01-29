# Crear una app que devuelva los numero primos entre 0 y el numero que le pasamos
'''
Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, que si intentamos dividirlos por cualquier otro número, el resultado no es entero. Dicho de otra forma,
si haces la división por cualquier número que no sea 1 o él mismo, se obtiene un resto distinto de cero.
'''

def es_primo(num):
    '''
    a continuaicon verificamos que el numero pasado no pueda dividirse por ningun numero
    entre 2 y ese mismo numero - 1
    '''
    for i in range(2, num-1):
        # si es divisible por alguno retornamo False y termina el bucle
        #print(f'i vale: {i}')
        if num % i == 0:
            #print(f'num % i = {num%i}')
            return False
    # si termina el bucle, significa que no fue divisible entonces es primo
    return True

def primos_hasta(num):
    primos = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)
    return primos

resultado = primos_hasta(13)
print(resultado)
