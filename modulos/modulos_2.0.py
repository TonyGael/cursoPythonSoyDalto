import sys
# import modulos_extra.saludar as saludar

# print(saludar.saludar_espanol('Tony'))
# print(saludar.saludar_ingles('Tony'))
print(sys)
print(sys.builtin_module_names)
print(sys.path)
sys.path.append('/home/user/Documents/pythonSoyDalto/modulos_extra')
print(sys.path)

import saludar as mod_saludo

print(mod_saludo.saludar_espanol('Tony'))
print(mod_saludo.saludar_ingles('Tony'))
