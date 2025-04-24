
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value ("Hello there") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("hey there !")
    assert value("How is it going")
def test_other():
    assert value("What's up") == 100
    assert value("What's going on ") == 100
    assert value("yo bro!") == 100

