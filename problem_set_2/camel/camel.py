# In a file called camel.py, implement a program
# that prompts the user for the name of a variable
# in camel case and outputs the corresponding name
# in snake case. Assume that the user's input will
# be in camel case.


def main():
    print(convert(input("camelCase: ").strip()))


def convert(s):
    snake_case = ""

    for char in s:
        if char.islower():
            snake_case += char
        elif char.isupper():
            snake_case += "_"
            snake_case += char.lower()

    return snake_case


if __name__ == "__main__":
    main()