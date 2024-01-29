# Ejercicio 1-a
# Promedio duración de cursos Python en YouTube
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

# Diferencias de duración entre cursos
print("------------------------")
dif_con_min = 100 - dalto_curso / otros_cursos_min * 100
print(f'El curso de Dalto dura un {dif_con_min}% menos que el más rápido')

# dif_con_max = 100 - dalto_curso / otros_cursos_max * 100
# print(f'El curso de Dalto dura un {round(dif_con_max, 2)}% menos que el más lento')

dif_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
print(f'El curso de Dalto dura un {dif_con_max}% menos que el más lento')

dif_con_prom = 100 - dalto_curso / otros_cursos_prom * 100
print(f'El curso de Dalto dura un {dif_con_prom}% menos que el promedio')
print("------------------------")
# Ejercicio 1-b
# Duración de videos en crudo
crudo_promedio = 5
crudo_dalto = 3.5

# Calculamos el porcentaje de tiempo vacio e relaciona los crudos:
tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 // crudo_promedio / 10
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío')

tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10
print(f'Este curso eliminó el {tiempo_vacio_dalto}% de tiempo vacío.')
print("------------------------")

# Ejercicio 1-c: Ver 10 horas de este curso a cuantas de otros cursos equivale? ¿Y al revés?
horas_dalto_cursos = otros_cursos_prom * 100  // dalto_curso / 10
print(f'Ver 10 horas del curso de Dalto equivale a ver {horas_dalto_cursos} de otros cursos')

horas_otros_cursos = dalto_curso * 100  // otros_cursos_prom / 10
print(f'Ver 10 horas del curso de los otros cursos equivale a ver {horas_otros_cursos} del curso de Dalto')
