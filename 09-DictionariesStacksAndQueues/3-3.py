import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   # Create a stack using LifoQueue
    stack = queue.LifoQueue()

    # Dictionary to map closing brackets to their matching opening brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}

    # Iterate over each character in the expression
    for char in expression:
        if char in '({[':  # Opening brackets
            stack.put(char)
        elif char in ')}]':  # Closing brackets
            if stack.empty():  # If stack is empty, it means there's no matching opening bracket
                return False
            top = stack.get()  # Pop the top of the stack
            if top != matching_bracket[char]:  # Check if it matches the corresponding opening bracket
                return False

    # If stack is empty, all brackets are matched
    return stack.empty()

if brackets_ok(expression1):
    print("Expression 1: Brackets are correct.")
else:
    print("Expression 1: Brackets are not correct.")

if brackets_ok(expression2):
    print("Expression 2: Brackets are correct.")
else:
    print("Expression 2: Brackets are not correct.")

if brackets_ok(expression3):
    print("Expression 3: Brackets are correct.")
else:
    print("Expression 3: Brackets are not correct.")