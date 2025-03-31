
total_amount = 50
inserted_coin = 0

while inserted_coin < total_amount:
    amount_due = total_amount - inserted_coin

    coin = int(input(f"Amount due :{amount_due} cents \nInsert coin"))



    if coin in [25,10,4]:
        inserted_coin += coin
    else:
        print("invalid")
change_owe = inserted_coin - total_amount
if change_owe > 0:
    print("Change owe{change_owe} cents")


