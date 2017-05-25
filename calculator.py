"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

def parse_token(input_token):
    for i in range(1, len(input_token)):
        if input_token[i].isdigit():
            input_token[i] = int(input_token[i])
        else:
            input_token = ["error"]
            break
    return input_token

print "Welcome to calculator!"

while True:
    user_input = raw_input("> ")
    token = user_input.split()
    token = parse_token(token)
    token[0] = token[0].lower()
    if token[0] == 'q':
        break
    elif token[0] == "+":
        print add(token[1], token[2])
    elif token[0] == "-":
        print subtract(token[1], token[2])
    elif token[0] == "*":
        print multiply(token[1], token[2])
    elif token[0] == "/":
        print divide(token[1], token[2])
    elif token[0] == "square":
        print square(token[1])
    elif token[0] == "cube":
        print cube(token[1])
    elif token[0] == "pow":
        print power(token[1], token[2])
    elif token[0] == "mod":
        print mod(token[1], token[2])
    else:
        print "Exiting with invalid input."
        break
