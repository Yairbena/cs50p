# In meal.py, implement a program that prompts the user
# for a time and outputs whether it's breakfast time,
# lunch time, or dinner time. If it's not time for a meal,
# don't output anything at all. Assume that the user's
# input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal's time range is inclusive.
# For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or
# anytime in between, it's time for breakfast.


def main():
    print(convert(input("What time is it? ").strip()))


def convert(time):
    hour, minutes = map(int, (time.split(":")))
    minutes_in_decimal = minutes / 60
    
    time_in_decimal = hour + minutes_in_decimal

    if 7 <= time_in_decimal <= 8:
        return "Breakfast time"
    elif 12 <= time_in_decimal <= 13:
        return "Lunch time"
    elif 18 <= time_in_decimal <= 19:
        return "Dinner time"
    else:
        return "Not a time to eat!"


if __name__ == "__main__":
    main()