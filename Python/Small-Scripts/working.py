import re

def main():
    time = input("time: ")
    print(convert(time))

def convert(time):
    matches = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", time)
    if not matches:
        raise ValueError
        
    hour1 = int(matches.group(1))
    hour2 = int(matches.group(4))
    min1 = int(matches.group(2)) if matches.group(2) else 0
    min2 = int(matches.group(5)) if matches.group(5) else 0
    p1 = matches.group(3)
    p2 = matches.group(6)

    if not (1 <= hour1 < 13) or not (1 <= hour2 < 13):
        raise ValueError
    if not (0 <= min1 < 60) or not (0 <= min2 < 60):
        raise ValueError

    if p1 == "AM":
        hour1 = 0 if hour1 == 12 else hour1
    else:
        hour1 = 12 if hour1 == 12 else hour1 + 12

    if p2 == "AM":
        hour2 = 0 if hour2 == 12 else hour2
    else:
        hour2 = 12 if hour2 == 12 else hour2 + 12
    

    return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"


if __name__ == "__main__":
    main()
