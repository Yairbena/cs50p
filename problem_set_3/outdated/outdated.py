# In a file called outdated.py, implement a program that
# prompts the user for a date, anno Domini, in month-day-year
# order, formatted like 9/8/1636 or September 8, 1636, wherein
# the month in the latter might be any of the values in the 
# list below. Then output that same date in YYY-MM-DD format. 
# If the user's input is not valid date in either format, 
# prompt the user again. Assume that every month has no more 
# than 31 days; no need to validate whether a month has 28, 29, 
# 30, or 31 days.


import re


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    print(get_date())


def get_date():
    while True:
        date = input("Date: ").strip()
        numeric_date_pattern = re.compile(r"^(0?[1-9]|1[0-2])/(3[0-1]|[1-2][0-9]|0?[1-9])/([0-9]{4})$")
        written_date_pattern = re.compile(r"(" + "|".join(months) + r") (3[0-1]|[1-2][0-9]|0?[1-9]), [0-9]{4}") 

        if numeric_date_pattern.match(date):
            month, day, year = map(int, date.split("/"))

            return f"{year:04}-{month:02}-{day:02}"
        
        elif written_date_pattern.match(date):
            month, day, year = date.split(" ")
            day, year = map(int, (day.rstrip(","), year))

            return f"{year}-{months.index(month) + 1:02}-{day:02}"
        
        else:
            continue


if __name__ == "__main__":
    main()