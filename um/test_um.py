import pytest
from um import count

def test_count_1():
    assert count("um") == 1

def test_count_2():
    assert count("Um") == 1

def test_count_3():
    assert count("Hello, um, world.") == 1

def test_count_4():
    assert count("yummy") == 0

def test_count_5():
    assert count("Um, thanks, um...") == 2

def test_count_6():
    assert count("um?") == 1
