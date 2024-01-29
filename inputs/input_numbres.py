# Asking for numbers at the prompt
number = input("Give me a number: ")

# Multipliying the number by 2
number_by_2 = number * 2 # concatenate the number as a string
print(f'2 times {number} as a string is equal to: {number_by_2}')

# We must parse the character 2 to number
number_by_2 = int(number) * 2
print(f'2 times {number} as an int number is equal to: {number_by_2}')

# Conerting the number to float
number_by_2 = float(number) * 2
print(f'2 times {number} as a float number is equal to: {number_by_2}')
