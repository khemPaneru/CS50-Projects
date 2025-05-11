import pytest
from um import count

def test_count_1():
    assert count("um") == 1

def test_count_2():
    assert count("umm, Hello") == 1

def test_count_3():
    assert count("yummy") == 0

def test_count_(4):
    assert count("um?") == 1
def test_count_5():
    assert count("Um, thanks, um...") == 2
