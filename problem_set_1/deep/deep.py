# In deep.py, implement a program that prompts the
# user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the
# user inputs 42 or (case-insensitively) forty-two or
# forty two. Otherwise output No.


def main():
    print(check_input(input("What is the Answer to the Great Question of Life, the Universe, and Everythong? ").lower().strip()))


def check_input(s):
    return "Yes" if s in ["42", "forty-two", "forty two"] else "No"
    

if __name__ == "__main__":
    main()
    
          