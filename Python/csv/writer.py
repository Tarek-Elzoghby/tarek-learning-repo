import csv

def main():
    headers_ = ["item", "quantity", "price", "total_price"]
    total_price = 0

    with open("sales.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames= headers_)
        writer.writeheader()
        while True:
            try:
                item = input("Item: ")
                try:
                    quantity = int(input("quantity: "))
                except ValueError:
                    print("input a number")
                    continue
                try:
                    price = float(input("price: "))
                except ValueError:
                    print("input a number")
                    continue
            except EOFError:
                break
            else:
                total_price = quantity * price
                writer.writerow({"item" : item, "quantity": quantity, "price": price, "total_price" : total_price})
        

if __name__ == "__main__":
    main()



