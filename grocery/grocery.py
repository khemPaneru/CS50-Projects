def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip()
            if item:  # If the input is not empty
                item = item.lower()
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1  # Initialize count
        except EOFError:
            break

    # sorted() helps to Sort dictionary keys alphabetically
    sorted_items = sorted(grocery_list.values())

    for item in sorted_items:
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()
