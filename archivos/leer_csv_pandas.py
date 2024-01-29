import pandas as pd
# # print(type(pd))

# df = pd.read_csv('./archivos/texto.csv', names = ["Name", "Lastname", "Age"]) # df de data frame
df = pd.read_csv('./archivos/datos.csv') # df de data frame
df2 = pd.read_csv('./archivos/datos.csv')


# print(df)

# # Obteniendo los datos de una columna
# # print(f'Columna nombres:\n{df["Name"]}')

# cadena = "0123456789"
# print(cadena[0])
# print(cadena[:])
# print(cadena[:5])
# print(cadena[-5:-1])
# print(cadena[1:10:2])

# nombres = df["nombre"]
# print(nombres)

# apellidos = df["apellido"]
# print(apellidos)

# ordenamos el data farme por edad asscendente
df_edad_asc = df.sort_values("edad")
print(df_edad_asc)

# ordenamos el data farme por edad descendente
df_edad_desc = df.sort_values("edad", ascending= False)
print(df_edad_desc)

# concatenando
df_concatenado = pd.concat([df,df2])
print(df_concatenado)

# accediendo a las primeras filas con head
primeras_filas = df.head(3)
print(primeras_filas)

# accediendo a las ultimas filas con tails
ultimas_filas = df.tail(3)
print(ultimas_filas)

# acceder a la cantidad de filas y columnas totales
filas_columnas_totales = df.shape
print(filas_columnas_totales)

# accediendo a filas y columnas desde la posición
filas_totales = df.shape[0]
columnas_totales = df.shape[1]
print(filas_totales)
print(columnas_totales)

# desempaquetando
filas_totales, columnas_totales = df.shape

print(filas_totales)
print(columnas_totales)

# algunas funciones as complejas
# obteniendo data estadística del dataframe
# describe
df_info = df.describe()
print(df_info)

# ahora accedermos a un elemento especifco del df con loc
print(f'Trabajando con: \x1B[3mproperty DataFrame.loc\x1B[0m :')
elem_espec_loc = df.loc[2, "edad"]
print(elem_espec_loc)

# ahora accedermos a un elemento especifco del df con iloc
print(f'Trabajando con: \x1B[3mproperty DataFrame.iloc\x1B[0m :')
elem_espec_iloc = df.iloc[2, 2]
print(elem_espec_iloc)

# accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
print(apellidos)

# accediendo a todas las filas de una fila
fila3 = df.loc[2,:]
print(fila3)

# tambien funciona con iloc, acediendo a filas cn edad mayor a 30
mayor_30 = df.loc[df["edad"]>30,:]
print(mayor_30)
