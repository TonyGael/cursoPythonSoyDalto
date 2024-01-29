def frase(nombre, apellido, adjetivo):
    return f'Qué hacés {nombre} {apellido}?! sos un {adjetivo}!!!'

frase_resultante = frase('Tony', 'Gael', 'Crack')
print(frase_resultante)

def frase_2(nom, ape, adj):
    return f'Qué hacés {nom} {ape}?! sos un {adj}!!!'

# utilizando keywords argument
frase_resultante_2 = frase_2(adj = "Capo", ape = "Gael", nom = "Tony")
print(frase_resultante_2)

def frase_3(nombre, apellido, adjetivo='Crack'):
    return f'Qué hacés {nombre} {apellido}?! sos un {adjetivo}!!!'

frase_resultante_3 = frase_3("Gael","Tony")
print(frase_resultante_3)

frase_resultante_3 = frase_3("Gael","Tony", "Inteligente")
print(frase_resultante_3)
