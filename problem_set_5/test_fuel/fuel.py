# In a file called fuel.py, reimplement Fuel Gauge from 
# Problem Set 3, restructuring your code per the below, 
# wherein:
# - convert expects a str in X/Y format as input, wherein 
# each of X and Y is an integer, and returns that fraction 
# as a percentage rounded to the nearest int between 0 and 
# 100, inclusive. If X and/or Y is not an integer, or if X 
# is greater than Y, then convert should raise a ValueError. 
# - gauge expects an int and returns a str that is:
# * "E" if that int is less than or equal to 1,
# * "F" if that int is greater than or equal to 99,
# * and "Z%" otherwise, wherein Z is that same int.


def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            numerator, denominator = map(int, fraction.split("/"))
            if denominator == 0 or numerator > denominator:
                raise ValueError
            
            percentage = convert(fraction)
            print(gauge(percentage))

            break
        
        except ValueError:
            continue
         
    
def convert(fraction: str) -> int:
    numerator, denominator = map(int, fraction.split("/"))   
    if denominator == 0:
        raise ZeroDivisionError
    
    percentage = round(numerator / denominator * 100)
    
    return percentage



def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    

if __name__ == "__main__":
    main()