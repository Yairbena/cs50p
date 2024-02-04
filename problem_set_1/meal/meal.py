# In meal.py, implement a program that prompts the user
# for a time and outputs whether it's breakfast time,
# lunch time, or dinner time. If it's not time for a meal,
# don't output anything at all. Assume that the user's
# input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal's time range is inclusive.
# For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or
# anytime in between, it's time for breakfast.
# CHALLENGE: If up for a challenge, optionally add support
# for 12-hour times, allowing the user to input times in
# these formats too:
# #:## a.m. and ##:## a.m.
# #:## p.m. and ##:## p.m.

import re
import sys


def main():
    time_in_decimal = convert(input("What time is it? ").strip())

    if 7 <= time_in_decimal <= 8:
        print("breakfast time")
    elif 12 <= time_in_decimal <= 13:
        print("lunch time")
    elif 18 <= time_in_decimal <= 19:
        print("dinner time")
    else:
        print("Not a time to eat!")


def convert(time):
    twelve_hours_pattern = re.match("^(1[0-2]|0?[0-9])\:[0-5][0-9] ([ap]\.m\.)?$", time, re.IGNORECASE)
    twenty_four_hours_pattern = re.match("^(2[0-4]|1[0-9]|0?[0-9])\:[0-5][0-9]$", time)

    if not twelve_hours_pattern and not twenty_four_hours_pattern:
        sys.exit("Invalid input")

    if twenty_four_hours_pattern:
        hour, minutes = map(int, time.split(":"))
    else:
        hour, minutes_apm = time.split(":")
        minutes, apm = minutes_apm.split(" ")
        hour, minutes = map(int, (hour, minutes))
        if apm.lower() == "p.m.":
            hour = hour + 12

    time_in_decimal = hour + minutes / 60

    return time_in_decimal


if __name__ == "__main__":
    main()