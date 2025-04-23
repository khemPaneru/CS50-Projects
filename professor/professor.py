
import random

def main():
    score = 0
    difficulty = get_level()

    for _ in range(10):
        X = generate_integer(difficulty)
        Y = generate_integer(difficulty)

        for attempt in range(3):
            try:
                answer = int(input(f"{X} + {Y} = "))
                if answer == X + Y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            # After 3 incorrect attempts
            if attempt == 2:
                print(f"{X} + {Y} = {X + Y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level_input = int(input("Level: "))
            if level_input in [1, 2, 3]:
                return level_input
        except ValueError:
            pass


def generate_integer(lvl):
    if lvl == 1:
        return random.randint(0, 9)
    elif lvl == 2:
        return random.randint(10, 99)
    elif lvl == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid ")


if __name__ == "__main__":
    main()
