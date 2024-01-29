'''Tenemos dos listas, una con nombres y otra con apellidos
escribir los datos en un archivo de texto de forma óptima
con un for
'''
nombres = ['Tony', 'Marylin', 'Julia', 'Guillermo', 'Vanesa']
apellidos = ['Gael', 'Häser', 'Duarte', 'Terlaak', 'Pereyra']

with open("./resolviendo_problemas/nombres_apellidos.txt", "w") as archivo:
    archivo.writelines('Los datos son:\n-----------\n')
    # for n,a in zip(nombres, apellidos):
    #     archivo.writelines(f'Nombre: {n}\nApellido: {a}\n-----------\n')
    [archivo.writelines(f'Nombre: {n}\nApellido: {a}\n-----------\n') for n,a in zip(nombres, apellidos)]

