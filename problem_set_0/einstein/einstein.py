# In a file called einstein.py, implement a
# program in Python that prompts the user for
# for mass as an integer (in kilograms) and
# then outputs the equivalent number of Jouls
# as an integer. Assume that the user will
# input and integer.


C = 300000000


def main():
    print("E:",calculate(input("m: ")))


def calculate(m):
    result = int(m) * pow(C, 2)

    return result


if __name__ == "__main__":
    main()




if __name__ == "__main__":
    main()