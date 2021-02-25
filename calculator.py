"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    
    print("Hi! These are the calculator functions: '+', '-', '*', '/'(divide), 'square', 'cube', 'pow'(power of), 'mod'")
    print("Please enter a calculation using the format __ e.g. cube 2 3 or press 'q' to quit:")
    user_input = input("> ")
    tokens = user_input.split(' ')
    print(tokens)

    if 'q' in tokens:
        break

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = '0'
    else:
        num2 = tokens[2]

    if operator == "+":
       result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    return result


operation = tokens[0]
num1 = int(tokens[1])
num2 = int(tokens[2])






















# def tokenize(operation, num1, num2):
#     if tokens[0] != "q":
#         if operation == 'pow':
#             return power(num1, num2)
#     else:
#         print('blah')

# print(operation)
# print(num1)
# print(num2)
# print(tokenize(operation, num1, num2))



# def tokenize(num1, num2): 
#     tokens[1] = num1
#     tokens[2] = num2
#     if tokens[0] == "q":
#         break
#     else:
#         if tokens[0] == "pow":
#             return power(num1, num2)

# print(tokenize(num1, num2))
# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens


