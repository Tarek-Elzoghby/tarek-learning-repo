from datetime import date
from num2words import num2words
import sys


def main():
    birth_day = input("Date of Birth: ")

    # return the result in minutes using English words instead of numerals
    minutes = num2words(calculate(birth_day)) 
    minutes = minutes.replace(" and ", " ")

    print(f"{minutes} minutes")


# test the input in the right format
def validateDate(birth_day):
    try:
        year, month, day = birth_day.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        birth = date(year, month, day)
    except ValueError:
        sys.exit(1)

    return birth


# calculate the time for the input day at midnight to the current day midnight
def calculate(birth):
    birth_date = validateDate(birth)
    today = date.today()
    old = today - birth_date
    old = round(old.total_seconds() / 60) 
    
    if old <= 0:
        sys.exit(1)
    return old



if __name__ == "__main__":
    main()
