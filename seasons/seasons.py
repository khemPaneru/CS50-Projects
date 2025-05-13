
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
