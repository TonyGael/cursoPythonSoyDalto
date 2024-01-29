# cambiar el tipo de dato de una columna en un archivo csv

import pandas as pd
df = pd.read_csv("/home/user/Documents/pythonSoyDalto/resolviendo_problemas/datos.csv")

df2 = pd.read_csv("./resolviendo_problemas/datos_2.csv")

# controlamos que haya abierto y leído bien el archivo csv
# print(df)

df['edad'] = df['edad'].astype(str)
print(df['edad'])
print(df['edad'][0])
print(type(df['edad'][0]))

# reemplazo de datos
df['apellido'].replace('dalto', 'Soydalto', inplace=True)
print(df['apellido'])

# eliminando fila con datos faltanets en datos_2 mediante df2 y dropna
print(df2)
df2 = df2.dropna()
print(df2)

# eliminando filas repetidas
df2 = df2.drop_duplicates()
print(df2)

# creando un dataframe con el dataframe resultante en limpio
df.to_csv("./resolviendo_problemas/datos_limpios.csv")
