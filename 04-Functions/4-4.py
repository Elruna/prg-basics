###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    str_number = str(number)
    sumf = 0
    for char in str_number:
        sumf = sumf + int(char)
    return sumf

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')