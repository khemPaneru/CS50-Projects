def main():
    total_amount = 50
    inserted_coin = 0

    while inserted_coin < total_amount:

        amount_due = total_amount - inserted_coin

        coin = int(input(f"Amount Due: {amount_due} \nInsert Coin: "))

        if coin in [25, 10, 5]:
            inserted_coin += coin
        else:
            print("Invalid coin. Please insert a valid coin (25, 10, or 5 cents).")

    change_owed = inserted_coin - total_amount

    print(f"Change Owed: {change_owed}")
main()
