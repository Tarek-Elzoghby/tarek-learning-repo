import pyfiglet
import sys
import random


def main():
    f = pyfiglet.Figlet()

    text = input("input: ")
    if len(sys.argv) == 1:
        print(pyfiglet.figlet_format(text, font=random.choice(f.getFonts())))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            try:
                f.setFont(sys.argv[2])
            except TypeError:
                print("invalid usage")
                sys.exit()
            else:
                print(f.renderText(text))
        else:
            print("invalid usage")
            sys.exit()

    else:
        sys.exit()


main()
