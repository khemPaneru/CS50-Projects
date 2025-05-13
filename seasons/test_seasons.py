import pytestfrom seasons import calculate_minutes, convert_to_words
from datetime import date, timedelta

def test_calculate_minutes():
    today = date.today()
    one_day_ago = today - timedelta(days=1)
    assert calculate_minutes(one_day_ago) == 1440  # 1 day = 1440 minutes

    two_days_ago = today - timedelta(days=2)
    assert calculate_minutes(two_days_ago) == 2880

def test_convert_to_words():
    assert convert_to_words(1440) == "one thousand four hundred forty"
    assert convert_to_words(525600) == " Five hundred twenty-seven thousand forty minutes"
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"
