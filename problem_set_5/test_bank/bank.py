# in a file called bank.py, reimplement "Home Federal Savings Bank" from Problem Set 1, 
# restructuring your code per the below, wherein value expect a str as input and return 
# an int, namely 0 if that str starts with "hello", 20 if that str starts with an "h" 
# (but not "hello"), or 100 otherwise, treating the str case-insensitively. You can 
# assume that the string passed to the value function will not contain any leading 
# spaces. Only main should print.


def main():
    greeting = input("Greeting: ").lower().strip()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()