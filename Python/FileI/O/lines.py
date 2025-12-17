import sys


def main():
    # Check the name of the program in CLA
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("missing file name")
        sys.exit(1)

    # Exit the program in case of there is more than one argument
    if len(sys.argv) != 2:
        print("too many arguments")
        sys.exit(2)

    # Exit the program if it is not a python file
    if not file_name.endswith(".py"):
        print("not a python file")
        sys.exit(3)

    count = 0
    # Open the file and count how many line there
    try:
        with open(file_name, "r") as file:
            for row in file:
                striped = row.lstrip()
                # Do not count comments and blank line
                if not striped.startswith("#") and striped:
                    count += 1
    # Exit the program if the file does not exist
    except FileNotFoundError:
        print("File Not Found")
        sys.exit(4)
       
    print(count)

if __name__ == "__main__":
    main()

