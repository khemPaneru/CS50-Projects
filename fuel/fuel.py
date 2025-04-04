def main():
    while True:
        try:

            user_input = input("Fraction: ")

            x, y = user_input.split('/')

            x = int(x)
            y = int(y)

            if x > y:
                raise ValueError
            if y == 0:
               raise ZeroDivisionError

            break
        except ValueError:
            print("parts can't be greater than whole" )

        except ZeroDivisionError:
            print("Total can't be zero")

    percentage = (x / y) * 100

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{round(percentage)}%")
main()
