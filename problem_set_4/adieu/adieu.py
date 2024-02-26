# in a file called adieu.py, implement a program that prompts
# the user for names, one per line, until the user inputs 
# control-d. Assume that the user will input at least one name.
# Then bid adieu to those names, seperating two names with one 
# and, three names with two commas and one and, and n names with
# n - 1 commas and one and, as in the below.


import inflect


def main():
    inlfect_names()


def inlfect_names():
    names = []
    try:
        while True:
            name = input("Name: ").strip().title()
            names.append(name)

    except EOFError:
        p = inflect.engine()
        inflected_names = p.join(names)
        print("Adieu, adieu, to", inflected_names)


if __name__ == "__main__":
    main()