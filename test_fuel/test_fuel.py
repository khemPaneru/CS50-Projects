
def main():
    while True:
        try:
           user_input = input("Fraction: ")
           percentage = convert(user_input)
           print


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            rasie ValueError
            


def gauge(percentage):



if __name__ == "__main__":
    main()
