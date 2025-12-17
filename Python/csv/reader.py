import csv

def main():
    with open("sales.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['item']} : {row['quantity']} : {row['price']}")

if __name__ == "__main__":
    main()