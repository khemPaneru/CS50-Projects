from datetime import date
import inflect

def main():
    birth_str = input("Date of Birth (YYYY-MM-DD): ")

    try:
        birth_date = parse_date(birth_str)
    except ValueError:
        print("Invalid date")
        return  # Graceful return instead of exit(1)

    today = date.today()
    minutes = calculate_minutes(birth_date, today)
    words = convert_to_words(minutes)
    print(f"{words} minutes")


def parse_date(date_str):
    try:
        year, month, day = map(int, date_str.strip().split('-'))
        return date(year, month, day)
    except Exception:
        raise ValueError("Invalid date format")


def calculate_minutes(birth_date, today):
    delta = today - birth_date
    return round(delta.days * 24 * 60)


def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="").capitalize()

if __name__ == "__main__":
    main()
