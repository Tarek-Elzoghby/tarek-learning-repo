import csv
import logging
import sys


def main():
    logging.basicConfig(
        filename="scourgify.log",  # save logs to a file
        level=logging.INFO,  # record INFO and higher
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    # implement a program that expects exactly 2 command-line argument
    if len(sys.argv) != 3:
        logging.error("Not the right number of command line argument")
        sys.exit()

    # exit the program if the file’s name does not end in .csv
    reader_name = sys.argv[1]
    writer_name = sys.argv[2]

    if not reader_name.endswith(".csv") or not writer_name.endswith(".csv"):
        logging.error("Not a csv file")
        sys.exit()

    headers = ["first name", "last name", "house"]

    # Open the csv file
    try:
        with open(reader_name, "r") as file, open(writer_name, "w", newline='') as new_file:
            logging.info(
                "program start, the reading file is opened and the writing file is created"
            )
            reader = csv.DictReader(file)
            logging.info("the file has been stored in a variable called reader")
            # fill the the rows in the file
            # make the headers of the csv file
            writer = csv.DictWriter(new_file, fieldnames=headers)
            writer.writeheader()
            logging.info("headers has been written")
            for row in reader:
                # split the name and change the positions of the first and last name
                try:
                    last, first = row["name"].split(",")
                    house = row["house"]
                except IndexError:
                    logging.error("name is too big or too small")
                    sys.exit()
                else:
                    # write the data in the new order in the new file
                    writer.writerow(
                        {"first name": first, "last name": last, "house": house}
                    )
        logging.info("the program end")
    # Exit the program if the file nor found
    except FileNotFoundError:
        logging.error("File not found")
        sys.exit()


if __name__ == "__main__":
    main()
