
from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_format():
    assert validate("127.0.0") == False
    assert validate("256.256.256.256") == False
    assert validate("cat") == False
    assert validate("1.2.3.1000") == False
    assert validate("1234.5.6.7") == False
    assert validate("...") == False
def test_out_of_range():
    assert validate("275.3.6.28") == False
    assert validate("300.1.2.3") == False
    assert validate("192.168.1.256") == False
