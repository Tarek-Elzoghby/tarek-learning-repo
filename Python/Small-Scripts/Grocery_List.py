items = []
def main():
    get_item()

    #sorted alphabetically by item
    new_list = sorted(items)
    count_list = []

    for i in new_list:

        #if the item is counted do not count it again
        if i not in count_list:
            count_list.append(i)

            count = new_list.count(i)
            print(f"{count} {i}")
            

    
def get_item():
    while True:
        #prompts the user for items, until the user inputs control-z
        try:
            item = input().strip().upper()
        except EOFError:
            break
        else:
            items.append(item)


main()