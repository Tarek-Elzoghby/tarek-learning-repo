months = [
    "January", "February",  "March",     "April",   "May",      "June",
    "July",    "August",    "September", "October", "November", "December"
]
def main():
    #expermenting
    new_format = standard()
    print(f"{new_format[0]}-{new_format[1]:02}-{new_format[2]:02}")




def standard ():
    #prompt the user for a date
    while True:
        date = input("Date: ")
        #in case the user used '/' format
        if "/" in date:
            try:
                month, day, year = date.split("/")
            except ValueError:
                print("not a valid date")
                continue
            else:
                month = int(month)
                day = int(day)
                year = int(year)
                if 0 < day <= 31 and 0 < month < 13:
                    return year, month, day
        #in case the user used the written format
        else:
            try:
                a_day, year = date.split(",")
                month, day = a_day.split()
            except ValueError:
                print("not a valid date")
                continue
            #making sure the user write a month in his input
            else:
                month = month.title()
                day = int(day)
                year = int(year)
                if month in months and 0 < day <= 31:
                    return year, months.index(month) + 1, day
                else:
                    continue

main()