"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    user_input = raw_input(">")
    user_input = user_input.split(" ")
    operator = user_input[0]

    if len(user_input) == 2:
        num1 = int(user_input[1])
        if operator == "square":
            print square(num1)
        elif operator == "cube":
            print cube(num1)

    elif len(user_input) == 3 and operator is not "/":
        num1 = int(user_input[1])
        num2 = int(user_input[2])

        if operator == "+":
            print add(int(user_input[1]), int(user_input[2]))

        elif operator == "-":
            print subtract(num1, num2)

        elif operator == "*":
            print multiply(num1, num2)

        elif operator == "pow":
            print power(num1, num2)

        elif operator == "mod":
            print mod(num1, num2)

        elif operator == "cubes+":
            print add_cubes(num1, num2)

    elif len(user_input) == 3 and operator == "/":
        num1 = float(user_input[1])
        num2 = float(user_input[2])
        print divide(num1, num2)

    elif len(user_input) == 4:
        num1 = int(user_input[1])
        num2 = int(user_input[2])
        num3 = int(user_input[3])

        if operator == "x+":
            print add_mult(num1, num2, num3)

    elif operator.upper() == "Q" or operator.upper() == "QUIT":
        break

    else:
        print "That's not a valid option, please choose again"
