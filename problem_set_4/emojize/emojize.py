# In a file called emojize.py, implement a program that prompts
# the user for a str in English and then outputs the "emojized"
# version of that str, converting any codes (or aliases) therein
# to their corresponsing emoji.


import emoji


def main():
    print("Output:", (convert(input("Input: ").strip().lower())))


def convert(s):
    return emoji.emojize(s, language="alias")


if __name__ == "__main__":
    main()