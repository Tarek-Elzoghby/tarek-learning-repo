def main():
    price = 50
    coins = [5, 10, 25]

    while True:
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue


        if coin in coins:
            price -= coin
            if price > 0:
                print(f"Amount Due: {price}")
                continue
            else:
                change = -price
                print(f"Change Owed: {change}")
                break
        else:
            print(f"Amount Due: {price}")



    

   




main()