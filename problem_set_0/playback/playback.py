# In a file called playback.py, implement a program in
# Python that prompts the user for input and then outputs
# that same input, replacing each space with ... (i.e., 
# three periods).


def main():
    print(whitespaces_to_periods(input()))


def whitespaces_to_periods(s):
    result = s.replace(" ", "...")
    
    return result


if __name__ == "__main__":
    main()
