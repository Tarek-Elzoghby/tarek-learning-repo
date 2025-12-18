import csv
import logging
import sys
from tabulate import tabulate

def main():
    logging.basicConfig(
        filename= "pizza.log",  # save logs to a file
        level=logging.INFO,            # record INFO and higher
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


    # implement a program that expects exactly one command-line argument
    if len(sys.argv) != 2:
        logging.error("Not the right number of command line argument")
        sys.exit()

    # exit the program if the file’s name does not end in .csv
    name = sys.argv[1]
    if not name.endswith(".csv"):
        logging.error("Not a csv file")
        sys.exit()

    # Open the csv file
    try:
        with open(name, "r") as file:
            logging.info("program start, the file is open")
            reader = csv.DictReader(file)

            # Outputs a table formatted as ASCII art using tabulate
            print(tabulate(reader, headers="keys"))
            logging.info("program end")

    except FileNotFoundError:
        logging.error("File not found")
        sys.exit()

if __name__ == "__main__":
    main()

