from datetime import date
import inflect
import sys
import re

def main():
    birth_str = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth_date = parse_date(birth_str)
    except ValueError as e:
        sys.exit(f"Invalid date: {e}")

    minutes = calculate_minutes(birth_date, date.today())
    words = convert_to_words(minutes)
    print(f"{words} minutes")

def parse_date(date_str):
    # Validate format with regex first
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise ValueError("Invalid format (use YYYY-MM-DD)")

    try:
        year, month, day = map(int, date_str.split('-'))
        birth_date = date(year, month, day)
        if birth_date > date.today():
            raise ValueError("Birth date cannot be in the future")
        return birth_date
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")

def calculate_minutes(birth_date, today):
    delta = today - birth_date
    return round(delta.total_seconds() / 60)

def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="").capitalize()

if __name__ == "__main__":
    main()
