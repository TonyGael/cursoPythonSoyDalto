#import modulos_extra.modulo_saludar as m_saludar # modulo_saludar es un objeto namespace
from modulo_saludar import saludar_espanol as in_spanish, saludar_ingles as saludar_ingles
# from modulo_saludar import *

#saludo = m_saludar.saludar('Gael')

saludo_espanol = in_spanish('Tony')
saludo_ingles = saludar_ingles('Tony')
print(saludo_espanol)
print(saludo_ingles)


