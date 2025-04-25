from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("OUTATIME") == False  # too long

def test_start_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False
    assert is_valid("50CS") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True

def test_number_rules():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50A") == False

def test_alphanumeric():
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
