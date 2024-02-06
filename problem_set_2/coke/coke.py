# Suppose that a machine sells bottles of Coca-Cola (Coke)
# for 50 cents and only accepts coins in these
# denomincations: 25 cents, 10 cents, and 5 cents.
# In a file called coke.py, implement a program that
# prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, 
# output how many cents in change the user is owed.
# Assume that the user will only input integers, and
# ignore any integer that isn't an accepted denomination.


def main():
    coins = [25, 10, 5]
    amount_due = 50
    change_owed = 0

    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: ").strip())
        
        if coin in coins:            
            if amount_due < coin:
                change_owed = coin - amount_due
            
            amount_due -= coin
    
    print("Change Owed:", change_owed)


# def main():
#     amount_due = 50
#     change_owed = 0
#     valid_coins = [25, 10, 5]

#     while amount_due > 0:
#         amount_due = int(input("Amount Due: "))
        
#         coin = int(input("Insert Coin: "))

#         if coin in valid_coins:
#             if amount_due < coin:
#                 change_owed = abs(amount_due - coin)
#             amount_due -= coin

#     print("Change Owed: ", change_owed)


if __name__ == "__main__":
    main()

