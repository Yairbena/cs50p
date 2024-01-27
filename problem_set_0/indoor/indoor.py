# In a file called indoor.py, implement a program
# in Python that prompts the user for input and then
# outputs that same input in lowercase. Punctuation
# and whitespace should be outputted unchanged. You're
# welcome but not required, to prompt the user explicitly,
# as by passing a str of your own as an argument to input.


def main():
    print(convert_to_lowercase(input()))


def convert_to_lowercase(s):
    return s.lower()


if __name__ == "__main__":
    main()