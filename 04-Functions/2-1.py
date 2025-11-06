# Program for testing built-in functions

# Finding the largest number from a set of numbers
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7,5,6,3,8,2 is', max_number)

# Finding the smallest number from a set of numbers
min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4,7,2,3,9,8 is', min_number)

# Finding the length of a string
str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

# Reading a letter from the keyboard (in this case, we assume user input)
# For the sake of the program, we simulate it by using input
letter = input('Please enter a letter: ')  # Waits for user input
print('You entered the letter:', letter)

# Converting a string "20303" to an integer
num_from_str = int("20303")
print('Integer representation of "20303" is', num_from_str)

# Converting the decimal number 304 to a binary string
binary_str = bin(304)
print('Binary representation of 304 is', binary_str)

# Converting the decimal number 304 to a hexadecimal string
hex_str = hex(304)
print('Hexadecimal representation of 304 is', hex_str)

# Getting the integer Unicode code of the Euro sign €
unicode_euro = ord('€')
print('Unicode code point for € is', unicode_euro)

# Calculating the absolute value of -17
abs_value = abs(-17)
print('The absolute value of -17 is', abs_value)