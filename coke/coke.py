def main():

    total_amount = 50
    inserted_coin = 0

    while inserted_coin < total_amount:
        amount_due = total_amount - inserted_coin

        coin = int(input(f"Amount Due :{amount_due}  \nInsert Coin: "))

        if coin in [25,10,5]:
            inserted_coin += coin
        else:
            print("amount_due")

    change_owe = inserted_oin - total_amount

    if change_owe > 0:
        print("Change Owed:{change_owe} cents")

main()
