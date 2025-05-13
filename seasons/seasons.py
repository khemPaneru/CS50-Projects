from datetime import date
import inflect
import sys

def main():
    birth_str = input("Date of Birth (YYYY-MM-DD): ")

    try:
        birth_date = parse_date(birth_str)
    except ValueError as e:
        sys.exit("Invalid date")

    today = date.today()
    minutes = calculate_minutes(birth_date, today)
    words = convert_to_words(minutes)
    print(f"{words} minutes")

def parse_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        birth_date = date(year, month, day)
        if birth_date > date.today():
            raise ValueError("Birth date cannot be in the future")
        return birth_date
    except:
        raise ValueError("Invalid date format")

def calculate_minutes(birth_date, today):
    delta = today - birth_date
    return round(delta.total_seconds() / 60)  # More precise

def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="").capitalize()

if __name__ == "__main__":
    main()
