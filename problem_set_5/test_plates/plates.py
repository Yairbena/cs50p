# in a file called plates.py, reimplement Vanity Plates from
# Problem Set 2, restructuring your code per the below, wherein
# is_valid still expects a str as input and returns True if that
# str meeets all requirements and False if it does not, but main 
# is only called if the value of __name__ is "__main__":


import string


def main():
    plate = input("Plate: ").strip().upper()
    print("Valid") if is_valid(plate) else print("Invalid")


def is_valid(plate):
    min_char = 2
    max_char = 6

    # plate plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if not min_char <= len(plate) <= max_char:
        return False

    # all plate plates must start with at least two letters
    if not plate[:2].isalpha():
        return False

    # numbers cannot be used in the middle of a plate; they must come at the end.
    # the first number used cannot be a '0'
    plate_digits = ""
    for i in range(min_char, len(plate)):
        if plate[i].isdigit():
            plate_digits += plate[i]
            if not plate[i:].isdigit():
                return False
            elif plate[i] == "0" and plate_digits.startswith("0"):
                return False
        # no periods, spaces, or punctuation marks are allowed
        if plate[i] in string.punctuation or plate[i].isspace():
            return False

    return True


if __name__ == "__main__":
    main()





# def main():
#     plate = input("Plate: ").strip()
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

#     print(is_valid(input("Plate: ").strip()))


# def is_valid(s):
#     if not s[0:2].isalpha():
#         return False

#     if not 2 <= len(s) <= 6:
#         return False
    
#     x = 2
#     for char in s[x:]:
#         if char.isdigit():
#             if not s[x:].isdigit() or s[x-1+len(char):].startswith("0"):
#                 return False

#     if not s.isalnum():
#         return False
    
#     return True


# if __name__ == "__main__":
#     main()