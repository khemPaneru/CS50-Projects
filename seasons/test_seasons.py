from seasons import get_date, get_minutes, number_to_words
from datetime import date, timedelta
import pytest


def test_get_date_valid():
    assert get_date("2000-01-01") == date(2000, 1, 1)


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("January 1, 2000")
    with pytest.raises(ValueError):
        get_date("2000-13-01")
    with pytest.raises(ValueError):
        get_date("2000-01-32")


def test_get_minutes():
    # Test with a known date (1 day = 1440 minutes)
    test_date = date.today() - timedelta(days=1)
    assert get_minutes(test_date) == 1440

    test_date = date.today() - timedelta(days=2)
    assert get_minutes(test_date) == 2880


def test_number_to_words():
    assert number_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert number_to_words(1051200) == "One million, fifty-one thousand, two hundred"
    assert number_to_words(0) == "Zero"
