
#copy one

def main():
    while True:
        try:
           user_fraction  = input("Fraction: ")
           fuel_percentage  = convert(user_fraction)
           print(gauge(fuel_percentage))
           break
        except(ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
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
