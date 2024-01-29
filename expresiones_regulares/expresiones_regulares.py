import re

texto = """Hola papá! esta es la cadena 1. cómo dice... que está mi camarada?
Esta es. La segunda línea de texto
Y esta es la final definitiva capitán
"""

resultado = re.search("Hola", texto)
print(resultado)

resultado_2 = re.findall("esta", texto, flags= re.IGNORECASE)
print(resultado_2)

# haciendo una busqueda simple
# \d busca digitos numericos del 0 - 9
resultado_d = re.findall(r'\d', texto)
print(resultado_d)

# \D busca TODO menos digitos numericos del 0 - 9
resultado_D = re.findall(r'\D', texto)
print(resultado_D)

#\w busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado_w = re.findall(r'\w', texto)
print(resultado_w)

#\W busca TODO caracteres alfanumericos [a-z A-Z 0-9 _]
resultado_W = re.findall(r'\W', texto)
print(resultado_W)

#\s busca espacios en blanco -> espacios, tabs, saltos de línea
resultado_s = re.findall(r'\s', texto)
print(resultado_s)

#\S busca TODO espacios en blanco -> espacios, tabs, saltos de línea
resultado_S = re.findall(r'\S', texto)
print(resultado_S)

# . busca TODO menos saltos en línea
resultado_punto = re.findall(r'.', texto)
print(resultado_punto)

# \n busca saltos en línea
resultado_salto_linea = re.findall(r'\n', texto)
print(resultado_salto_linea)

# \ cancelar caracteres especiales, cancelando la funicon del punto y buscandi puntos
resultado_cancela_puntos = re.findall(r'\.', texto)
print(resultado_cancela_puntos)

# armando una cadena que busque un numero, seguido de un punto y un espacio
resultado_busca_1 = re.findall(r'\d\.\s', texto)
print(resultado_busca_1)
