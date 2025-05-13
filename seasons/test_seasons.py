import pytest
from datetime import date
from seasons import calculate_minutes, convert_to_words

def test_calculate_minutes():
    # Example test case: assume the user was born on a known date
    birthdate_str = "2000-01-01"
    birth_date = parse_date(birthdate_str)  # Parsing the birthdate string to a date object
    today = date.today()  # Using today's date

    # Calculating expected minutes for one year
    expected_minutes = round((today - birth_date).days * 24 * 60)

    # Run the function with the correct arguments
    assert calculate_minutes(birth_date, today) == expected_minutes  # Test should pass now

def test_convert_to_words():
    # Test converting a number to words
    assert convert_to_words(525600) == "five hundred twenty-five thousand six hundred"

if __name__ == "__main__":
    pytest.main()
