def main():
    grocery_list = {}
    while True:
        try:
            item = input().strip()
            if item: # If the user input is not empty
                item = item.lower
                if item in grocery_list:
                    grocery_list += item
                else:
                    grocery_list = 1
            except EOFError:
                break
    sorted_items = sorted(grocery_list.keys())

    for item in sorted_items:
        print(f"{grocery_list[item] } {item.upper()}")
