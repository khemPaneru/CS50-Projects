
def main():
    while True:
        try:
           user_input = input("Fraction: ")
           Total_percentage = convert(user_input)
           print(gauge(Total_percentage))


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            rasie ValueError
        calculated_percentage = round((X / y) * 100)
            return calculated_percentage

    except(ValueError, ZeroDivisionError)
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage > = 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
