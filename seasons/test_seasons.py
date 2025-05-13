from unittest.mock import patch
from datetime import date, timedelta
import pytest
from seasons import calculate_minutes, convert_to_words, main


def test_calculate_minutes():
    today = date.today()
    one_day_ago = today - timedelta(days=1)
    assert calculate_minutes(one_day_ago, today) == 1440  # 1 day = 1440 minutes

    two_days_ago = today - timedelta(days=2)
    assert calculate_minutes(two_days_ago, today) == 2880


def test_convert_to_words():
    assert convert_to_words(1440) == "one thousand four hundred forty"
    assert convert_to_words(525600) == "five hundred twenty-five thousand six hundred"
    assert convert_to_words(1051200) == "one million fifty-one thousand two hundred"


@patch('builtins.input', return_value='1990-01-01')  # Mock input for testing
def test_main(mock_input):
    with patch('sys.exit') as mock_exit:
        main()
        mock_exit.assert_not_called()  # Ensure sys.exit() is not called
