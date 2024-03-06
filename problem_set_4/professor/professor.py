# in a file called professor.py, implement a program that:
# - Prompts the user for a level, n. If the user does not input 1, 2, or 3,
# the program should prompt again.
# - Randomly generates ten (10) math problems formatted as X + Y =, wherein
# each of X and Y is a non-negative integer with n figits. No need to support 
# operation other than addition (+).
# - Prompts the user to solve each of those problems. If an answer is not 
# correct (or not even a number), the program should output EEE and prompt the 
# user again, allowing the user up to three tries in total for that problem. 
# If the user has still not answered orrectly after three tries, the program 
# should output the correct answer.
# - The program should ultimately output the user's score: the number of 
# correct answers out of 10.


import random


def main():
    level = get_level()
    
    score = 0
    for i in range(0,10):
        x, y = generate_integer(level), generate_integer(level)
        
        mistakes = 0
        while mistakes < 3:
            answer = input(f"{x} + {y} = ")
            
            if answer.isdigit() and (x + y) == int(answer):
                score += 1
                break
            else:
                print("EEE")
                mistakes += 1
                if mistakes == 3:               
                    print(f"{x} + {y} = {x + y}")
    
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return level


def generate_integer(level):
    level = int(level)
    if level == 1:
        min_range = 0
    else:
        min_range = 10 ** (level - 1)
    
    max_range = (10 ** level) - 1
    
    return random.randint(min_range, max_range)


if __name__ == "__main__":
    main()