# In a file called grocery.py, implement a program
# that prompts the user for items, one per line, until 
# the user inputs control-d (which is a common way of 
# ending one's input to a program). Then output the user's 
# grocery list in all uppercase, sorted alphabetically by 
# item, perfixing each line with a number of times the user 
# inputted that item. No need to pluralize the items. Treat 
# the user's input case-insensitively.


def main():
    groceries = {}

    try:
        while True:
            grocery = input()

            if grocery in groceries:
                groceries[grocery] += 1
            else:
                groceries[grocery] = 1

    except EOFError:    
        for grocery in sorted(groceries):
            print(groceries[grocery], grocery.upper())


if __name__ == "__main__":
    main()