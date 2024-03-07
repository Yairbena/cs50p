# in a file called bitcoin.py, implement a program that:
# - Expects the user to specify as a command-line argument the number of
# Bitcoins, n, that they would like to buy. If that argument cannot be 
# converted to a float, the program should exit via sys.exit with an 
# error message.
# - Queries the API for the CoinDesk Bitcoin Price Index at
# https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON
# object, among whose nested keys in the current price of Bitcoin as a 
# float. Be sure to catch any exceptions, as with code like:
# import requests
# try:
#     ...
# except requests.RequestsException:
#     ...
# - Outputs the current cost of n Bitcoins in USD to four decimal places, 
# using , as a thousands separator.


import requests
import sys


def main():
    qty = float(validate_arg())

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    response = requests.get(url)
    if not response.status_code == 200:
        print("Failed to retrieve data from the API", response.status_code)
                
    try: 
        data = response.json()

    except requests.RequestException:
        sys.exit("Failed to decode text into json")
    
    rate = float(data["bpi"]["USD"]["rate_float"])
    print(f"${qty * rate:,.4f}")


def validate_arg():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    try:
        if float(sys.argv[1]):
            qty = sys.argv[1]
            
            return qty

    except ValueError:
        sys.exit("Command-line argument is not a number")
        

if __name__ == "__main__":
    main()