###city = 'Krakow' for char in city: print(char)
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    number_str = str(number)
    sum_dig = 0
    for i in number_str:
        sum_dig = sum_dig + int(i)
    return sum_dig

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')