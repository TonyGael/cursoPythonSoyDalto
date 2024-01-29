import re

#detectando un numero Posadas y ocultandolo
texto = "Hola Cristian, mi numero es: +54 3764-110177"

pattern = r'\+\d{2}\s\d{4}-\d{6}'

remplazo = re.sub(pattern,"(Número oculto)",texto)

print(remplazo)