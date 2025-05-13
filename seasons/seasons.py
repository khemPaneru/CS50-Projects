from datetime import date
import inflect

def main():
    birth_str = input("Date of Birth(YYYY-MM-DD): ")

    try:
        birth_date = parse_date(birth_str)
    except ValueError:
        print("Invalid date")  # Print the error message
        return  # End the function without raising an exit error

    # Use actual today in normal run
    today = date.today()
    minutes = calculate_minutes(birth_date, today)
    words = convert_to_words(minutes)
    print(f"{words} minutes")


def parse_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        return date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date format")


def calculate_minutes(birth_date, today):
    delta = today - birth_date
    return round(delta.days * 24 * 60)


def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="").capitalize()

if __name__ == "__main__":
    main()
