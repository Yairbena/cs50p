# In a file called game.py, implement a program that:
# - Prompts the user for a level, n. If the user does not 
# input a positive integer, the program should prompt again.
# - Randomly generates an integer between 1 and n, inclusive, 
# using the random module.
# - Prompts the user to guess that integer. If the guess is 
# not positive integer, the program should prompt the user 
# again.
#   - If the user is smaller than that integer, the program 
#     should output Too small! and prompt the user again.
#   - If the guess is larger than that integer, the program 
#     should output Too large! and prompt the user again.
#   - If the guess is the same as that integer, the program 
#     should output Just right! and exit.


import random
import sys


def main():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if not 0 < level <= sys.maxsize:
                raise ValueError
            break

        except ValueError:
            continue

    hidden_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if hidden_number > guess:
                print("Too small!")
            elif hidden_number < guess:
                print("Too large!")
            else:
                print("Just right!")
                break

        except ValueError:
            continue


if __name__ == "__main__":
    main()