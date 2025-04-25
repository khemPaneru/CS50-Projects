
from plates import is_valid

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("CS50PY") == True
    assert is_valid("CS50python") == False

def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False

def test_numbers_end():
    assert is_valid("Cs50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS5O0") == False

def test_no_special_characters():
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
