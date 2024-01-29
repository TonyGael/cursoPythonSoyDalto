# cerando una funcion simple
def saludar():
    print("Hello fulano!")

saludar()

def saludar_bis(nombre, genero):
    genero = genero.lower()
    if (genero == 'mujer'):
        adjetivo = 'reina'
    elif (genero == 'hombre'):
        adjetivo = 'lobo'
    else:
        adjetivo = 'amigue'
        
    print(f'Hola {nombre}!')

saludar_bis('Cristian', 'hombre')
saludar_bis('Marylin', 'mujer')
saludar_bis('Cacho', 'amiguite')

#crear una funcion que nos retorne valores
def crear_password_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    password = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    #print(password)
    return(password, num)

#password = crear_password_random(398)
password, primer_num = crear_password_random(398)
#frase = f'Tu nueva pass es: {password}'
print(f'Tu nueva pass es: {password}')
print(f'El número utilizado para crearla es: {primer_num}')
