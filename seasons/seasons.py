
from datetime import data
import inflect
import sys

def main():
    birth_str = input("Date of Birth(YYYY-MM-DD: "))

    try:
        birth_date = parse_date(birth_str):
    except ValueError:
        sys.exit("Invalid date")


def parse_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        return date(year, month, day)
    except:
        raise ValueError("Invalid date format")

def calculate_minutes(birth_date):
    today = date.today()
    delta = today - birth_date
    return round(delta.days * 24 * 60)

def convert_to_words(number):
    p = inflect.engine()
    return p.number
