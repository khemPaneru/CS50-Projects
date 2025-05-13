from seasons import parse_date, calculate_minutes, convert_to_words
from datetime import date, timedelta
import pytest

def test_parse_date_valid():
    assert parse_date("2000-01-01") == date(2000, 1, 1)

def test_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("January 1, 2000")
    with pytest.raises(ValueError):
        parse_date("2000-13-01")
    with pytest.raises(ValueError):
        parse_date("2000-01-32")
    with pytest.raises(ValueError):
        parse_date("3000-01-01")  # Future date

def test_calculate_minutes():
    test_date = date.today() - timedelta(days=1)
    assert calculate_minutes(test_date, date.today()) == 1440  # 1 day = 1440 minutes

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred"
