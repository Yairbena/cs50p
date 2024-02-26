# In a file called figlet.py, implement a program that:
# - Zero if the user would like to output text in a 
# random font.
# - Two if the user would like to output text in a 
# specific font, in which case the first of the two 
# should be -f or --font, and the second of the two 
# should be the name of the font.
# - Prompts the user for a str of text.
# - Outputs that text in the desired font.
# If the user provides two command-line arguments and 
# the first is not -f or --font or the second is not 
# the name of a font, the program should exit via 
# sys.exit with an error message.


from pyfiglet import Figlet
import random
import sys


def main():
    print("Output:", convert())


def convert():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    elif sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage.")

    s = input("Input: ").strip()

    return figlet.renderText(s)


if __name__ == "__main__":
    main()