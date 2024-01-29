# OPERADORES DE COMPARACIÓN:

# operador igual que ==
print("Operador igual que ==")
es_igual = 2023 == 2024
print(es_igual)
print('a' == 'A') #False
print(1 == '1') #False
print(1 == 1.0) # True
print(2.0 == 12/6) # True

# operador no es igual !=
print("Operador no es igual:")
print(1 != 1.0) #False
print(0 != 1) # True
print(10 != '10') # True
print(2.5 != 10/4) # False

# operador mayor que >
print("Operador mayor que >:")
print(5 > 3) #True
print('A' > 'a') #False
print('@' > '|') #False

# Operador menor que <
print("Operador menor que <:")
print(5 < 3) #False
print('A' < 'a') #True
print('@' < '|') #True

# Operador mayor o igual que >=
print("Operador mayor o igual que >=:")
print(1 >= 3) #False
print(1 >= 1.0) #True
print('.' >= ';') #False

# Operador menor o igual que <=
print("Operador menor o igual que <=:")
print(True <= True) #False
print('A' <= 'Á') #True
print(1.9 <= 1.999) #True
