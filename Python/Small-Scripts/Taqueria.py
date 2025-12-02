menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    #prompt the user to place an order.
    total = 0
    while True:
        order = get_item("Item: ")
        #After each inputted item, display the total cost of all items inputted thus far
        if order is None:
            print()
            break

        total = total + menu[order]
        print(f"${total:.2f}")
        
    

def get_item(prompt):
    while True:
        #prompts the user for items, until the user inputs control-z
        try:
            item = input(prompt).strip().title()
        except EOFError:
            return None
        else:
            #Ignore any input that isn’t an menu.
            if item in menu:
                return item
            else:
                continue
main()