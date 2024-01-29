def sumar_dos():
    while True:
        a = input('Número 1: ')
        b = input('Número 2: ')
        try:
            resultado = int(a) + int(b)
        except ValueError as e:
            print('Algo raro está pasando, ingrseaste solo números?')
            print(f'ERROR: {e}')
        else:
            break
        finally:
            print('Manejo de excepción finalizado')
    return resultado

print(sumar_dos())
