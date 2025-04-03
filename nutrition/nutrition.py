


fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        }

fruit = input("Item: ").lower()
if fruit in fruits:
    print(f"calories: {fruits[fruit]}")

