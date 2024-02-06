# When texting or tweeting, it's not uncommin to shorten words
# to save time or space, as by omitting vowels, such like 
# Twitter was originally called twttr. In a file called twttr.py,
# implement a program that prompts the user for a str of text and
# then outputs that same text but with all vowels 
# (A, E, I, O and U) omitted, whether inputted in uppercase or
# lowercase.


def main():
    print("Output:", omit_vowels(input("Input: ").strip()))


def omit_vowels(s):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    omitted_s = ""

    for char in s:
        if char not in vowels:
            omitted_s += char

    return omitted_s


if __name__ == "__main__":
    main()