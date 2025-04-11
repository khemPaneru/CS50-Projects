def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip()
            if item:  # If the input is not empty
                item = item.lower()  # Convert input to lowercase
                if item in grocery_list:
                    grocery_list[item] += 1  # Increase count
                else:
                    grocery_list[item] = 1  # Initialize count
        except EOFError:
            break  # Exit the loop when EOF is encountered

    # Sort dictionary keys alphabetically
    sorted_items = sorted(grocery_list.keys())

    # Print grocery list
    for item in sorted_items:
        print(f"{grocery_list[item]} {item.upper()}")

# Run the main function
if __name__ == "__main__":
    main()
