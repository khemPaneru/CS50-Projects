
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
        
