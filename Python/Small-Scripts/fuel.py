def main():
    fraction = get_fraction("Fraction: ") 
    print(get_percent(fraction))
    



def get_fraction(prompt):
    while True:
        x = input(prompt)
        try:
            z, y = x.split("/", 1)
            f = int(z)/int(y)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        else:
            if 1 >= f >= 0:
                return f
            else:
                continue

def get_percent(i):
    i = i *100
    if i <= 1:
        return "E"
    elif i >= 99:
        return "F"
    else:
        return f"{round(i)}%"
    




main()