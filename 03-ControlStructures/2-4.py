###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int( input() )
number2 = int( input() )
operator = input()
if operator == '+' :
    result = number1 + number2
elif operator == '-' :
    result = number1 - number2
elif operator == '*' :
    result = number1 * number2
elif operator == '/' :
    result = number1 / number2
    
print(result)