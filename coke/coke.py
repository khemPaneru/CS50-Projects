
total_amount = 50
insert_coin = 0

while insert_coin < total_amount:
    amount_due = total_amount - insert_coin

    result = int(input(f"Amount due :{amount_due}"))
    insert_coin += result
    print(f"Total inserted : {insert_coin}")


