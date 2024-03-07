# In a file called twttr.py, reimplement "Setting up my twttr" from Problem Set 2,
# restructuring your code per the below, wherein shorten expects a str as input 
# and returns that same str but with all vowels (A, E, I, O, and U) ommited, 
# whether inputted in uppercase or lowercase.
# def main():
#     ...
# def shorten():
#     ...
# if __name__ == "__main__":
#     main()


def main():
    text = input("Input: ").strip()
    print(shorten(text))


def shorten(text):
    vowels = "AEIOUaeiou"
    
    short = ""
    for c in text:
        if c not in vowels:
            short += c

    return short


if __name__ == "__main__":
    main()