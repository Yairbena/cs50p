import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():

    order_total = 0

    while True:
        try:
            item = input("Item: ").lower().strip()
        except EOFError:
            print("\n")
            sys.exit(0)

        for key in menu:
            if key.lower() == item:
                order_total += float(menu[key])
                print("Total: ${:.2f}".format(order_total))


if __name__ == "__main__":
    main()