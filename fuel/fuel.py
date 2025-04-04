def main():
    while True:
        try:

            user_input = input("Fraction: ")

            x, y = user_input.split('/')

            x = int(x)
            y = int(y)

            if x > y:
                print("Error: Num can't be greater than deno")
                continue
            if y == 0:
                print("Error: Denominator can't be 0.")
                continue
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction in the form x/y.")

    percentage = (x / y) * 100

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{round(percentage)}%")
main()
