#ing_mensual = 800
#ing_mensual = 800
ing_mensual = 12000
gasto_mensual = 7000

if ing_mensual > 10000:
    if ing_mensual - gasto_mensual > 3000:# ejemplo de if anidado
        print("Te sobra una platita!")
    else:
        print("deberías gastar menos.")
elif ing_mensual > 1000:
    print("Estás OK en latinoamérica")
else:
    print("Tenes una púa")
