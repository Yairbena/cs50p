# In a file called fuel.py, implement a program
# that prompts the user for a fraction, formatted
# as X/Y, wherein each of X and Y is an integer, 
# and then outputs, as a percentage rounded to the
# nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead
# to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to
# indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater
# than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4). Be sure to
# catch any excepion like ValueError or
# ZeroDivisionError


def main():
    print(get_percentage())


def get_percentage():        
    while True:
        try:
            fraction = input("Fraction: ").strip()
            numerator, denominator = map(int, fraction.split("/"))
            if denominator == 0:
                raise ZeroDivisionError
            if numerator > denominator:
                raise ValueError
             
            percentage = (numerator / denominator * 100)
            if 0 <= percentage <= 1:
                return "E"
            elif 99 <= percentage <= 100:
                return "F"
            else:
                return f"{round(percentage)}%"
            
        except ValueError:
            continue
        except ZeroDivisionError:
            continue


if __name__ == "__main__":
    main()