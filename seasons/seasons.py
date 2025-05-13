from datetime import date
import inflect

def main():
    birth_str = input("Date of Birth(YYYY-MM-DD): ")

    # Attempt to parse the date without printing anything or exiting on error
    birth_date = parse_date(birth_str)
    if not birth_date:  # If the date couldn't be parsed, return early without error message
        return

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
        return None  # Instead of raising an exception, return None if invalid format


def calculate_minutes(birth_date, today):
    delta = today - birth_date
    return round(delta.days * 24 * 60)


def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="").capitalize()

if __name__ == "__main__":
    main()
