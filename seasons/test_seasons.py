import pytest
from seasons import calculate_minutes, convert_to_words

def test_calculate_minutes():
    # Example test case: assume the user was born on a known date
    birthdate = "2000-01-01"
    assert calculate_minutes(birthdate) == 525600  # 1 year worth of minutes

def test_convert_to_words():
    # Test converting a number to words
    assert convert_to_words(525600) == "five hundred twenty-five thousand six hundred"

if __name__ == "__main__":
    pytest.main()
