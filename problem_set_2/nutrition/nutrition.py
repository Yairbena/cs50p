# In a file called nutrition.py, implement a program that 
# prompts users to input a fruit (case-insensitively) and
# the outputs the number of calories in one portion of 
# that fruit, per the FDA's poster for fruits, which is 
# also available as text. Capitalization aside, assume 
# that users will input fruits exactly as written in the 
# poster (e.g., strawberries, not strawberry). Ignore any 
# input that isn't a fruit.


fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 60,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}


def main():
    calories = get_calories(input("Item: ").strip().lower())
    if not calories == None:
        print(f"Calories: {calories}")


def get_calories(item):
    for fruit in fruits:
        if item == fruit:
            return fruits[fruit]


if __name__ == "__main__":
    main()