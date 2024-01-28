# In a file called interpreter.py, implement a program
# that prompts the user for an arthmetic expression
# and then calculates and outputs the result as a 
# floating-point value formatted to one decimal place.
# Assume that the user's input will be formatted as 
# x y z, with one space between x and y and one spece
# between y an z, wherein:
# - x is an integer.
# - y is +, -, *, or /
# - z is an integer
import re
import sys


def main():
    print(calculate(input("Expression: ")))


def calculate(expression):
    if not re.match(r"^[0-9]* [-+*/] [0-9]*$", expression):
        sys.exit("Invalid input")

    x, y, z = expression.split(" ")
    x, z = map(int, (x, z))
    
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        if z == 0:
            raise ZeroDivisionError
        else:
            result = x / z

    return float(result)


if __name__ == "__main__":
    main()
    